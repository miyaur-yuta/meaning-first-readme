from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Iterable

from .graph import MeaningGraph
from .model import ProjectConfig, SemanticBlock
from .text import estimate_tokens
from .validate import ValidationReport, validate_repository


@dataclass(frozen=True, slots=True)
class AuditReport:
    data: dict[str, object]
    validation: ValidationReport

    @property
    def passed(self) -> bool:
        gates = self.data["gates"]
        return self.validation.passed and all(bool(value) for value in gates.values())

    def to_dict(self) -> dict[str, object]:
        return {"passed": self.passed, **self.data, "validation": self.validation.to_dict()}


def audit_repository(
    config: ProjectConfig,
    blocks: Iterable[SemanticBlock],
    *,
    today: date | None = None,
) -> AuditReport:
    block_list = list(blocks)
    active = [block for block in block_list if block.active]
    validation = validate_repository(config, block_list, today=today)
    graph = MeaningGraph(active)

    factual = [block for block in active if block.kind in {"fact", "decision"}]
    traceable = [block for block in factual if block.evidence or block.source or block.depends_on]
    procedures = [block for block in active if block.kind == "procedure"]
    actionable = [block for block in procedures if block.acceptance]
    volatile = [block for block in active if block.volatile]
    fresh = [block for block in volatile if block.expires and (today or date.today()) <= block.expires]
    roots = [block.id for block in active if block.kind == "purpose"]
    reachable = graph.reachable_from(roots) if roots else set()
    orphans = sorted(block.id for block in active if block.id not in reachable)

    total_words = max(1, sum(len(re.findall(r"\w+", block.machine_text)) for block in active))
    ambiguity_count = sum(
        block.machine_text.casefold().count(term.casefold())
        for block in active
        for term in config.ambiguous_terms
        if term
    )
    ambiguity_per_1000 = ambiguity_count * 1000 / total_words

    evidence_blocks = [block for block in active if block.kind == "evidence"]
    evidence_backlinks = sum(1 for block in evidence_blocks if block.supports)
    authoritative = [block for block in active if block.trust == "authoritative"]

    dimensions = {
        "structure": {
            "active_blocks": len(active),
            "kinds": sorted({block.kind for block in active}),
            "required_kinds_present": all(kind in {block.kind for block in active} for kind in config.required_kinds),
            "estimated_tokens": sum(estimate_tokens(block.machine_text) for block in active),
        },
        "traceability": {
            "eligible_blocks": len(factual),
            "traceable_blocks": len(traceable),
            "ratio": len(traceable) / len(factual) if factual else 1.0,
            "evidence_blocks": len(evidence_blocks),
            "evidence_with_backlinks": evidence_backlinks,
        },
        "actionability": {
            "procedures": len(procedures),
            "procedures_with_acceptance": len(actionable),
            "ratio": len(actionable) / len(procedures) if procedures else 1.0,
        },
        "freshness": {
            "volatile_blocks": len(volatile),
            "fresh_volatile_blocks": len(fresh),
            "ratio": len(fresh) / len(volatile) if volatile else 1.0,
        },
        "connectivity": {
            "purpose_roots": roots,
            "reachable_blocks": len(reachable),
            "orphan_blocks": orphans,
            "ratio": len(reachable) / len(active) if active else 1.0,
        },
        "clarity": {
            "ambiguous_occurrences": ambiguity_count,
            "ambiguous_per_1000_words": round(ambiguity_per_1000, 3),
            "authoritative_blocks": len(authoritative),
        },
    }

    gates = {
        "no_validation_errors": validation.passed,
        "required_structure": bool(dimensions["structure"]["required_kinds_present"]),
        "full_traceability": dimensions["traceability"]["ratio"] == 1.0,
        "full_actionability": dimensions["actionability"]["ratio"] == 1.0,
        "fresh_volatile_data": dimensions["freshness"]["ratio"] == 1.0,
        "no_orphans": not orphans,
        "no_ambiguous_placeholders": ambiguity_count == 0,
    }

    return AuditReport(data={"dimensions": dimensions, "gates": gates}, validation=validation)


def render_audit_markdown(report: AuditReport) -> str:
    data = report.to_dict()
    lines = [
        "# Meaning Audit Report",
        "",
        f"**Result:** {'PASS' if report.passed else 'FAIL'}",
        "",
        "## Quality gates",
        "",
        "| Gate | Result |",
        "|---|---|",
    ]
    for gate, passed in data["gates"].items():
        lines.append(f"| `{gate}` | {'PASS' if passed else 'FAIL'} |")
    lines.extend(["", "## Dimensions", ""])
    for name, values in data["dimensions"].items():
        lines.append(f"### {name}")
        lines.append("")
        for key, value in values.items():
            lines.append(f"- **{key}:** `{value}`")
        lines.append("")
    if report.validation.issues:
        lines.extend(["## Validation findings", ""])
        for issue in report.validation.issues:
            location = f" [{issue.block_id}]" if issue.block_id else ""
            lines.append(f"- **{issue.severity.upper()} `{issue.code}`{location}:** {issue.message}")
    return "\n".join(lines).rstrip() + "\n"
