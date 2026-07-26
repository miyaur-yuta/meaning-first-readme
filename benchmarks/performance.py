#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import date
from pathlib import Path

from meaning_first_readme.compiler import render_readme
from meaning_first_readme.model import ProjectConfig, SemanticBlock
from meaning_first_readme.rank import select_context
from meaning_first_readme.snapshot import snapshot_data
from meaning_first_readme.validate import validate_repository


def max_rss_kib() -> int | None:
    """Return peak resident set size in KiB when the platform exposes it."""
    try:
        import resource
    except ImportError:
        if sys.platform != "win32":
            return None
        try:
            import ctypes
            from ctypes import wintypes
        except ImportError:
            return None

        class PROCESS_MEMORY_COUNTERS(ctypes.Structure):
            _fields_ = [
                ("cb", wintypes.DWORD),
                ("PageFaultCount", wintypes.DWORD),
                ("PeakWorkingSetSize", ctypes.c_size_t),
                ("WorkingSetSize", ctypes.c_size_t),
                ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPagedPoolUsage", ctypes.c_size_t),
                ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
                ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                ("PagefileUsage", ctypes.c_size_t),
                ("PeakPagefileUsage", ctypes.c_size_t),
            ]

        get_process_memory_info = ctypes.WinDLL("psapi").GetProcessMemoryInfo
        get_process_memory_info.argtypes = [
            wintypes.HANDLE,
            ctypes.POINTER(PROCESS_MEMORY_COUNTERS),
            wintypes.DWORD,
        ]
        get_process_memory_info.restype = wintypes.BOOL
        counters = PROCESS_MEMORY_COUNTERS()
        counters.cb = ctypes.sizeof(counters)
        handle = ctypes.WinDLL("kernel32", use_last_error=True).GetCurrentProcess()
        if not get_process_memory_info(handle, ctypes.byref(counters), counters.cb):
            return None
        return int(counters.PeakWorkingSetSize // 1024)

    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # macOS reports bytes; Linux reports KiB.
    if sys.platform == "darwin":
        return int(usage // 1024)
    return int(usage)


def make_blocks(count: int) -> list[SemanticBlock]:
    blocks = [
        SemanticBlock(
            id="purpose.synthetic",
            kind="purpose",
            title="Synthetic performance purpose",
            summary="Measure deterministic behavior on a large typed block collection.",
            body="This synthetic corpus exists only to measure parser-independent graph, validation, ranking, rendering, and snapshot performance.",
            priority=100,
            audience=("both",),
            tags=("performance", "synthetic"),
            trust="authoritative",
            updated=date(2026, 7, 26),
        )
    ]
    for index in range(1, count):
        topic = index % 97
        blocks.append(
            SemanticBlock(
                id=f"example.synthetic-{index:05d}",
                kind="example",
                title=f"Synthetic context example {index}",
                summary=f"Example {index} covers topic {topic} with a unique and searchable semantic unit.",
                body=(
                    f"This is synthetic block {index}. It belongs to topic {topic}. "
                    f"Its unique marker is item-{index:05d}-topic-{topic:02d}. "
                    "The body is intentionally long enough for duplicate detection and context ranking. "
                    "It represents a meaningful unit with a stable identifier and an explicit dependency."
                ),
                order=1000 + index,
                priority=20 + (index % 60),
                audience=("both",),
                tags=("synthetic", f"topic-{topic}", f"item-{index}"),
                trust="reviewed",
                depends_on=("purpose.synthetic",),
                updated=date(2026, 7, 26),
            )
        )
    return blocks


def make_config() -> ProjectConfig:
    return ProjectConfig(
        name="Synthetic Meaning First README",
        tagline="Performance corpus",
        language="en",
        content_dir=Path("."),
        required_kinds=("purpose",),
        required_blocks=("purpose.synthetic",),
        section_order=("purpose", "example"),
        mandatory_context_kinds=("purpose",),
        mandatory_context_blocks=("purpose.synthetic",),
        ambiguous_terms=("TBD", "TODO"),
        max_duplicate_similarity=0.92,
        benchmark_min_recall=0.8,
        benchmark_min_precision=0.2,
        max_context_tokens=32000,
        generated_notice="synthetic",
    )


def measured(function):
    start = time.perf_counter()
    value = function()
    return value, time.perf_counter() - start


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks", type=int, default=2000)
    parser.add_argument("--output", default="build/performance.json")
    args = parser.parse_args()
    if args.blocks < 2:
        parser.error("--blocks must be at least 2")

    blocks, create_seconds = measured(lambda: make_blocks(args.blocks))
    config = make_config()
    validation, validate_seconds = measured(lambda: validate_repository(config, blocks))
    selection, context_seconds = measured(
        lambda: select_context(
            config,
            blocks,
            task=f"find item {args.blocks - 1} topic {(args.blocks - 1) % 97}",
            budget=8000,
            audience="ai",
        )
    )
    readme, render_seconds = measured(lambda: render_readme(config, blocks))
    snapshot, snapshot_seconds = measured(lambda: snapshot_data(blocks))

    report = {
        "schema_version": 1,
        "block_count": args.blocks,
        "passed": validation.passed,
        "warning_count": len(validation.warnings),
        "error_count": len(validation.errors),
        "selected_context_blocks": len(selection.selected),
        "context_estimated_tokens": selection.estimated_tokens,
        "readme_bytes": len(readme.encode("utf-8")),
        "snapshot_digest": snapshot["repository_digest"],
        "seconds": {
            "create": round(create_seconds, 6),
            "validate": round(validate_seconds, 6),
            "context": round(context_seconds, 6),
            "render": round(render_seconds, 6),
            "snapshot": round(snapshot_seconds, 6),
            "total": round(create_seconds + validate_seconds + context_seconds + render_seconds + snapshot_seconds, 6),
        },
        "max_rss_kib": max_rss_kib(),
        "note": "Timing is environment-specific and is recorded as an observation, not a portable performance guarantee."
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if validation.passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
