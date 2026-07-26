from __future__ import annotations

from dataclasses import replace
from datetime import date
from pathlib import Path

from meaning_first_readme.model import ProjectConfig, SemanticBlock


def block(identifier: str = "purpose.test", **changes) -> SemanticBlock:
    base = SemanticBlock(
        id=identifier,
        kind="purpose",
        title="Test purpose",
        summary="A sufficiently descriptive summary for testing.",
        body="This is a sufficiently long body used by the test suite to represent a semantic block.",
        priority=80,
        audience=("both",),
        tags=("test",),
        status="active",
        trust="reviewed",
        updated=date(2026, 7, 26),
    )
    return replace(base, **changes)


def config(root: Path | None = None, **changes) -> ProjectConfig:
    base = ProjectConfig(
        name="Test Project",
        tagline="Meaning first.",
        language="en",
        content_dir=(root or Path.cwd()) / "content",
        required_kinds=("purpose",),
        required_blocks=("purpose.test",),
        section_order=("purpose", "scope", "constraint", "decision", "procedure", "evidence"),
        mandatory_context_kinds=("purpose",),
        mandatory_context_blocks=("purpose.test",),
        ambiguous_terms=("TBD", "TODO"),
        max_duplicate_similarity=0.90,
        benchmark_min_recall=0.80,
        benchmark_min_precision=0.20,
        max_context_tokens=32000,
        generated_notice="generated",
    )
    return replace(base, **changes)
