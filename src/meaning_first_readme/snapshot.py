from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .model import SemanticBlock
from .text import sha256_text


def block_record(block: SemanticBlock, *, include_body: bool = True) -> dict[str, object]:
    """Return a location-independent semantic record.

    Source paths are intentionally excluded so repository fingerprints remain
    stable when the same checkout is moved or cloned into another directory.
    """

    data = block.to_dict(include_body=include_body)
    data.pop("path", None)
    return data


def snapshot_data(blocks: Iterable[SemanticBlock]) -> dict[str, object]:
    records = []
    for block in sorted(blocks, key=lambda item: item.id):
        data = block_record(block)
        canonical = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        data["digest"] = sha256_text(canonical)
        records.append(data)
    aggregate = json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "schema_version": 1,
        "repository_digest": sha256_text(aggregate),
        "blocks": records,
    }


def write_snapshot(path: Path, blocks: Iterable[SemanticBlock]) -> dict[str, object]:
    data = snapshot_data(blocks)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return data


def load_snapshot(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))
