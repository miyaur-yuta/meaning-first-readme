from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Iterable

from .graph import MeaningGraph
from .model import (
    ALLOWED_AUDIENCES,
    ALLOWED_KINDS,
    ALLOWED_STATUSES,
    ALLOWED_TRUST,
    ProjectConfig,
    SemanticBlock,
)
from .text import canonical_claim, jaccard, shingles, simhash64, simhash_bands

INJECTION_PATTERNS = (
    re.compile(r"ignore (all |the )?previous instructions", re.I),
    re.compile(r"system prompt", re.I),
    re.compile(r"developer message", re.I),
    re.compile(r"これまでの(指示|命令)を無視"),
    re.compile(r"前の(指示|命令)を無視"),
)


@dataclass(frozen=True, slots=True)
class Issue:
    severity: str
    code: str
    message: str
    block_id: str = ""
    path: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "severity": self.severity,
            "code": self.code,
            "message": self.message,
            "block_id": self.block_id,
            "path": self.path,
        }


@dataclass(frozen=True, slots=True)
class ValidationReport:
    issues: tuple[Issue, ...]

    @property
    def errors(self) -> tuple[Issue, ...]:
        return tuple(issue for issue in self.issues if issue.severity == "error")

    @property
    def warnings(self) -> tuple[Issue, ...]:
        return tuple(issue for issue in self.issues if issue.severity == "warning")

    @property
    def passed(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, object]:
        return {
            "passed": self.passed,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "issues": [issue.to_dict() for issue in self.issues],
        }


def _issue(severity: str, code: str, message: str, block: SemanticBlock | None = None) -> Issue:
    return Issue(
        severity=severity,
        code=code,
        message=message,
        block_id=block.id if block else "",
        path=str(block.path) if block and block.path else "",
    )


def validate_repository(
    config: ProjectConfig,
    blocks: Iterable[SemanticBlock],
    *,
    today: date | None = None,
) -> ValidationReport:
    today = today or date.today()
    block_list = list(blocks)
    issues: list[Issue] = []

    ids: dict[str, SemanticBlock] = {}
    for block in block_list:
        if block.id in ids:
            issues.append(_issue("error", "duplicate-id", f"duplicate id: {block.id}", block))
        else:
            ids[block.id] = block

        if not re.fullmatch(r"[a-z][a-z0-9]*(?:[._-][a-z0-9]+)+", block.id):
            issues.append(_issue("error", "invalid-id", "id must be a stable dotted/lowercase identifier", block))
        if block.kind not in ALLOWED_KINDS:
            issues.append(_issue("error", "invalid-kind", f"unsupported kind: {block.kind}", block))
        if block.status not in ALLOWED_STATUSES:
            issues.append(_issue("error", "invalid-status", f"unsupported status: {block.status}", block))
        if block.trust not in ALLOWED_TRUST:
            issues.append(_issue("error", "invalid-trust", f"unsupported trust level: {block.trust}", block))
        invalid_audience = set(block.audience) - ALLOWED_AUDIENCES
        if invalid_audience:
            issues.append(_issue("error", "invalid-audience", f"unsupported audience: {sorted(invalid_audience)}", block))
        if not 0 <= block.priority <= 100:
            issues.append(_issue("error", "invalid-priority", "priority must be between 0 and 100", block))
        if len(block.summary.strip()) < 12:
            issues.append(_issue("warning", "weak-summary", "summary is too short to stand alone", block))
        if block.updated is None:
            issues.append(_issue("warning", "missing-updated", "updated date is not declared", block))
        if block.volatile and block.expires is None:
            issues.append(_issue("error", "volatile-without-expiry", "volatile blocks require expires", block))
        if block.active and block.expires and block.expires < today:
            issues.append(_issue("error", "expired-active-block", f"active block expired on {block.expires.isoformat()}", block))
        if block.kind == "fact" and not (block.evidence or block.source):
            issues.append(_issue("error", "fact-without-evidence", "facts require evidence references or a source", block))
        if block.kind == "decision" and not block.rationale.strip():
            issues.append(_issue("error", "decision-without-rationale", "decisions require a rationale", block))
        if block.kind == "procedure" and not block.acceptance:
            issues.append(_issue("error", "procedure-without-acceptance", "procedures require acceptance criteria", block))
        if block.kind == "evidence" and not block.supports:
            issues.append(_issue("warning", "orphan-evidence", "evidence should declare what it supports", block))
        if block.trust == "external_untrusted":
            for pattern in INJECTION_PATTERNS:
                if pattern.search(block.body):
                    issues.append(_issue("warning", "untrusted-instruction-pattern", "untrusted content contains instruction-like text and must remain quarantined", block))
                    break
        for term in config.ambiguous_terms:
            if term and term.casefold() in block.machine_text.casefold():
                issues.append(_issue("warning", "ambiguous-placeholder", f"ambiguous or unfinished term found: {term!r}", block))

    kinds = {block.kind for block in block_list if block.active}
    for required in config.required_kinds:
        if required not in kinds:
            issues.append(_issue("error", "missing-required-kind", f"no active block of required kind: {required}"))
    for required in config.required_blocks:
        if required not in ids or not ids[required].active:
            issues.append(_issue("error", "missing-required-block", f"required active block is missing: {required}"))

    graph = MeaningGraph(block_list)
    for source, relation, target in graph.missing_references():
        issues.append(_issue("error", "missing-reference", f"{relation} points to missing block {target}", ids.get(source)))
    for cycle in graph.cycles():
        issues.append(_issue("error", "dependency-cycle", " -> ".join(cycle.path), ids.get(cycle.path[0])))

    claim_owners: dict[str, list[SemanticBlock]] = {}
    negation_owners: dict[str, list[SemanticBlock]] = {}
    for block in block_list:
        if not block.active:
            continue
        for claim in block.claims:
            claim_owners.setdefault(canonical_claim(claim), []).append(block)
        for claim in block.negates:
            negation_owners.setdefault(canonical_claim(claim), []).append(block)
    for claim in sorted(set(claim_owners) & set(negation_owners)):
        positives = ", ".join(item.id for item in claim_owners[claim])
        negatives = ", ".join(item.id for item in negation_owners[claim])
        issues.append(_issue("error", "claim-contradiction", f"claim is asserted by [{positives}] and negated by [{negatives}]"))

    active = [block for block in block_list if block.active and len(block.body) >= 80]
    shingle_cache = {block.id: shingles(block.body) for block in active}
    by_active_id = {block.id: block for block in active}
    buckets: dict[tuple[int, int], list[str]] = {}
    exact_buckets: dict[frozenset[str], list[str]] = {}
    for block in active:
        features = shingle_cache[block.id]
        exact_buckets.setdefault(frozenset(features), []).append(block.id)
        for band in simhash_bands(simhash64(features), bands=8):
            buckets.setdefault(band, []).append(block.id)

    candidate_pairs: set[tuple[str, str]] = set()
    for identifiers in list(buckets.values()) + list(exact_buckets.values()):
        unique = sorted(set(identifiers))
        for index, left_id in enumerate(unique):
            for right_id in unique[index + 1 :]:
                candidate_pairs.add((left_id, right_id))

    for left_id, right_id in sorted(candidate_pairs):
        similarity = jaccard(shingle_cache[left_id], shingle_cache[right_id])
        if similarity >= config.max_duplicate_similarity:
            issues.append(
                _issue(
                    "warning",
                    "near-duplicate",
                    f"{left_id} and {right_id} similarity={similarity:.3f}",
                    by_active_id[left_id],
                )
            )

    for block in block_list:
        for evidence_id in block.evidence:
            evidence = ids.get(evidence_id)
            if evidence and evidence.kind != "evidence":
                issues.append(_issue("warning", "non-evidence-reference", f"evidence reference {evidence_id} has kind {evidence.kind}", block))
            if evidence and block.id not in evidence.supports:
                issues.append(_issue("warning", "evidence-backlink-missing", f"{evidence_id} does not list {block.id} in supports", block))

    severity_order = {"error": 0, "warning": 1, "info": 2}
    issues.sort(key=lambda item: (severity_order.get(item.severity, 9), item.code, item.block_id, item.message))
    return ValidationReport(tuple(issues))
