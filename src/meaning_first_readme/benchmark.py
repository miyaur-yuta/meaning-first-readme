from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .model import ProjectConfig, SemanticBlock
from .rank import mandatory_context_ids, select_context


@dataclass(frozen=True, slots=True)
class BenchmarkCaseResult:
    name: str
    query: str
    expected: tuple[str, ...]
    selected: tuple[str, ...]
    recall: float
    precision: float
    passed: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "query": self.query,
            "expected": list(self.expected),
            "selected": list(self.selected),
            "recall": self.recall,
            "precision": self.precision,
            "passed": self.passed,
        }


@dataclass(frozen=True, slots=True)
class BenchmarkReport:
    cases: tuple[BenchmarkCaseResult, ...]
    macro_recall: float
    macro_precision: float
    passed: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "passed": self.passed,
            "macro_recall": self.macro_recall,
            "macro_precision": self.macro_precision,
            "cases": [case.to_dict() for case in self.cases],
        }


def load_cases(path: Path) -> list[dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("benchmark file must contain a JSON array")
    return data


def run_benchmark(
    config: ProjectConfig,
    blocks: Iterable[SemanticBlock],
    cases: Iterable[dict[str, object]],
) -> BenchmarkReport:
    block_list = list(blocks)
    results: list[BenchmarkCaseResult] = []
    for raw in cases:
        name = str(raw["name"])
        query = str(raw["query"])
        expected = tuple(str(item) for item in raw["expected"])
        budget = int(raw.get("budget", 2200))
        audience = str(raw.get("audience", "ai"))
        selection = select_context(config, block_list, task=query, budget=budget, audience=audience)
        selected = selection.ids
        expected_set = set(expected)
        relevant_set = expected_set | mandatory_context_ids(config, block_list, audience=audience)
        selected_set = set(selected)
        hits = len(expected_set & selected_set)
        relevant_hits = len(relevant_set & selected_set)
        recall = hits / len(expected_set) if expected_set else 1.0
        precision = relevant_hits / len(selected_set) if selected_set else (1.0 if not relevant_set else 0.0)
        passed = recall >= float(raw.get("minimum_recall", config.benchmark_min_recall))
        results.append(
            BenchmarkCaseResult(
                name=name,
                query=query,
                expected=expected,
                selected=selected,
                recall=recall,
                precision=precision,
                passed=passed,
            )
        )
    macro_recall = sum(case.recall for case in results) / len(results) if results else 1.0
    macro_precision = sum(case.precision for case in results) / len(results) if results else 1.0
    passed = (
        all(case.passed for case in results)
        and macro_recall >= config.benchmark_min_recall
        and macro_precision >= config.benchmark_min_precision
    )
    return BenchmarkReport(tuple(results), macro_recall, macro_precision, passed)


def render_benchmark_markdown(report: BenchmarkReport) -> str:
    lines = [
        "# Context Retrieval Benchmark",
        "",
        f"**Result:** {'PASS' if report.passed else 'FAIL'}",
        f"**Macro recall:** `{report.macro_recall:.3f}`",
        f"**Macro precision:** `{report.macro_precision:.3f}`",
        "",
        "| Case | Recall | Precision | Result |",
        "|---|---:|---:|---|",
    ]
    for case in report.cases:
        lines.append(
            f"| {case.name} | {case.recall:.3f} | {case.precision:.3f} | {'PASS' if case.passed else 'FAIL'} |"
        )
    lines.append("")
    for case in report.cases:
        lines.extend(
            [
                f"## {case.name}",
                "",
                f"- Query: {case.query}",
                f"- Expected: {', '.join(case.expected)}",
                f"- Selected: {', '.join(case.selected)}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"
