from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Mapping

ALLOWED_KINDS = {
    "purpose",
    "scope",
    "non_goal",
    "definition",
    "principle",
    "assumption",
    "fact",
    "constraint",
    "decision",
    "architecture",
    "procedure",
    "evidence",
    "risk",
    "example",
    "glossary",
    "roadmap",
    "faq",
    "changelog",
}
ALLOWED_STATUSES = {"draft", "active", "deprecated", "superseded", "archived"}
ALLOWED_AUDIENCES = {"human", "ai", "both"}
ALLOWED_TRUST = {"authoritative", "reviewed", "unverified", "external_untrusted"}


@dataclass(frozen=True, slots=True)
class SemanticBlock:
    """A single independently addressable unit of meaning.

    The model deliberately separates typed metadata from prose.  This makes the
    README useful as both a human document and a machine-readable context graph.
    """

    id: str
    kind: str
    title: str
    summary: str
    body: str
    order: int = 1000
    priority: int = 50
    audience: tuple[str, ...] = ("both",)
    tags: tuple[str, ...] = ()
    status: str = "active"
    trust: str = "reviewed"
    depends_on: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    supports: tuple[str, ...] = ()
    claims: tuple[str, ...] = ()
    negates: tuple[str, ...] = ()
    acceptance: tuple[str, ...] = ()
    rationale: str = ""
    owner: str = ""
    source: str = ""
    updated: date | None = None
    expires: date | None = None
    volatile: bool = False
    path: Path | None = None
    extra: Mapping[str, Any] = field(default_factory=dict)

    @property
    def active(self) -> bool:
        return self.status == "active"

    @property
    def machine_text(self) -> str:
        metadata = " ".join(
            [self.id, self.kind, self.title, self.summary, *self.tags, *self.claims]
        )
        return f"{metadata}\n{self.body}".strip()

    def to_dict(self, *, include_body: bool = True) -> dict[str, Any]:
        data: dict[str, Any] = {
            "id": self.id,
            "kind": self.kind,
            "title": self.title,
            "summary": self.summary,
            "order": self.order,
            "priority": self.priority,
            "audience": list(self.audience),
            "tags": list(self.tags),
            "status": self.status,
            "trust": self.trust,
            "depends_on": list(self.depends_on),
            "evidence": list(self.evidence),
            "supports": list(self.supports),
            "claims": list(self.claims),
            "negates": list(self.negates),
            "acceptance": list(self.acceptance),
            "rationale": self.rationale,
            "owner": self.owner,
            "source": self.source,
            "updated": self.updated.isoformat() if self.updated else None,
            "expires": self.expires.isoformat() if self.expires else None,
            "volatile": self.volatile,
            "path": str(self.path) if self.path else None,
        }
        if include_body:
            data["body"] = self.body
        if self.extra:
            data["extra"] = dict(self.extra)
        return data


@dataclass(frozen=True, slots=True)
class ProjectConfig:
    name: str
    tagline: str
    language: str
    content_dir: Path
    required_kinds: tuple[str, ...]
    required_blocks: tuple[str, ...]
    section_order: tuple[str, ...]
    mandatory_context_kinds: tuple[str, ...]
    mandatory_context_blocks: tuple[str, ...]
    ambiguous_terms: tuple[str, ...]
    max_duplicate_similarity: float
    benchmark_min_recall: float
    benchmark_min_precision: float
    max_context_tokens: int
    generated_notice: str
    metadata: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, raw: Mapping[str, Any], *, root: Path) -> "ProjectConfig":
        project = raw.get("project", {})
        quality = raw.get("quality", {})
        context = raw.get("context", {})
        benchmark = raw.get("benchmark", {})
        render = raw.get("render", {})
        return cls(
            name=str(project.get("name", "Meaning First README")),
            tagline=str(project.get("tagline", "")),
            language=str(project.get("language", "ja")),
            content_dir=(root / str(project.get("content_dir", "content/blocks"))).resolve(),
            required_kinds=tuple(project.get("required_kinds", ("purpose", "scope"))),
            required_blocks=tuple(project.get("required_blocks", ())),
            section_order=tuple(project.get("section_order", tuple(ALLOWED_KINDS))),
            mandatory_context_kinds=tuple(
                context.get("mandatory_kinds", ("purpose",))
            ),
            mandatory_context_blocks=tuple(
                context.get("mandatory_blocks", ("purpose.meaning",))
            ),
            ambiguous_terms=tuple(
                quality.get("ambiguous_terms", ("TBD", "TODO", "あとで", "たぶん"))
            ),
            max_duplicate_similarity=float(
                quality.get("max_duplicate_similarity", 0.88)
            ),
            benchmark_min_recall=float(benchmark.get("minimum_recall", 0.80)),
            benchmark_min_precision=float(benchmark.get("minimum_precision", 0.35)),
            max_context_tokens=int(context.get("max_tokens", 32000)),
            generated_notice=str(
                render.get(
                    "generated_notice",
                    "This file is generated. Edit content/blocks instead.",
                )
            ),
            metadata={
                key: value
                for key, value in raw.items()
                if key not in {"project", "quality", "context", "benchmark", "render"}
            },
        )
