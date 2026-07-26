from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Iterable

from .model import ProjectConfig, SemanticBlock
from .snapshot import block_record, snapshot_data
from .text import estimate_tokens, sha256_text

KIND_LABELS = {
    "purpose": "目的",
    "scope": "対象範囲",
    "non_goal": "非目的",
    "definition": "定義",
    "principle": "原則",
    "assumption": "前提",
    "fact": "事実",
    "constraint": "制約",
    "decision": "意思決定",
    "architecture": "構造",
    "procedure": "手順",
    "evidence": "根拠",
    "risk": "リスク",
    "example": "例",
    "glossary": "用語",
    "roadmap": "ロードマップ",
    "faq": "FAQ",
    "changelog": "変更履歴",
}


def _anchor(value: str) -> str:
    return value.replace(".", "").replace("_", "-")


def render_block(block: SemanticBlock) -> str:
    marker_payload = json.dumps(
        {
            "id": block.id,
            "kind": block.kind,
            "priority": block.priority,
            "status": block.status,
            "digest": sha256_text(
                json.dumps(
                    block_record(block),
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )[:16],
        },
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    metadata = [
        f"`{block.id}`",
        f"種別: `{block.kind}`",
        f"優先度: `{block.priority}`",
        f"信頼区分: `{block.trust}`",
        f"対象: `{', '.join(block.audience)}`",
    ]
    if block.updated:
        metadata.append(f"更新: `{block.updated.isoformat()}`")
    if block.depends_on:
        metadata.append("依存: " + ", ".join(f"`{value}`" for value in block.depends_on))
    if block.evidence:
        metadata.append("根拠: " + ", ".join(f"`{value}`" for value in block.evidence))

    acceptance = ""
    if block.acceptance:
        acceptance = "\n\n**受け入れ条件**\n\n" + "\n".join(f"- [ ] {item}" for item in block.acceptance)
    rationale = ""
    if block.rationale:
        rationale = f"\n\n**判断理由:** {block.rationale}"
    return (
        f"<!-- mfr:block {marker_payload} -->\n"
        f"### {block.title}\n\n"
        f"> {block.summary}\n\n"
        f"<sub>{' · '.join(metadata)}</sub>\n\n"
        f"{block.body.strip()}"
        f"{rationale}{acceptance}\n\n"
        f"<!-- /mfr:block {block.id} -->\n"
    )


def render_readme(config: ProjectConfig, blocks: Iterable[SemanticBlock]) -> str:
    active = sorted((block for block in blocks if block.active), key=lambda item: (item.order, item.id))
    grouped: dict[str, list[SemanticBlock]] = defaultdict(list)
    for block in active:
        grouped[block.kind].append(block)

    snapshot = snapshot_data(active)
    repository_digest = str(snapshot["repository_digest"])
    max_updated = max((block.updated.isoformat() for block in active if block.updated), default="unknown")
    total_body_tokens = sum(estimate_tokens(block.machine_text) for block in active)

    available_kinds = [kind for kind in config.section_order if grouped.get(kind)]
    remaining = sorted(set(grouped) - set(available_kinds))
    kinds = available_kinds + remaining

    toc = ["## 目次", ""]
    for kind in kinds:
        label = KIND_LABELS.get(kind, kind)
        toc.append(f"- [{label}](#{_anchor(label)})")
        for block in grouped[kind]:
            toc.append(f"  - [{block.title}](#{_anchor(block.title)})")

    manifest = {
        "schema_version": 1,
        "project": config.name,
        "repository_digest": repository_digest,
        "latest_source_update": max_updated,
        "active_blocks": len(active),
        "estimated_source_tokens": total_body_tokens,
        "block_ids": [block.id for block in active],
    }

    header = f"""# {config.name}

> **{config.tagline}**

> [!IMPORTANT]
> **目的は「意味を達成すること」。長さは目的ではなく、必要な意味を失わず収容するための容量です。**

このREADMEは、人間とAIが同じ目的・境界・根拠・次の行動を再現できるように、型付きの意味ブロックからコンパイルされています。本文を直接編集せず、`content/blocks/`を更新してから品質ゲートを通してください。

| 項目 | 値 |
|---|---:|
| 有効な意味ブロック | {len(active)} |
| 推定ソーストークン | {total_body_tokens:,} |
| 最新ソース更新日 | {max_updated} |
| リポジトリ指紋 | `{repository_digest[:20]}` |
| 生成規約 | `{config.generated_notice}` |

<!-- mfr:manifest {json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))} -->

"""

    sections: list[str] = []
    for kind in kinds:
        label = KIND_LABELS.get(kind, kind)
        sections.append(f"## {label}\n")
        sections.extend(render_block(block) for block in grouped[kind])

    lightweight_manifest = {
        "schema_version": 1,
        "repository_digest": repository_digest,
        "blocks": [
            {
                **block_record(block, include_body=False),
                "digest": sha256_text(
                    json.dumps(
                        block_record(block),
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    )
                ),
            }
            for block in active
        ],
    }
    machine_manifest = json.dumps(lightweight_manifest, ensure_ascii=False, indent=2)
    footer = f"""
## 機械可読マニフェスト

<details>
<summary>AI・検証ツール向けの完全な意味グラフを表示</summary>

```json
{machine_manifest}
```

</details>

---

このREADMEの成否は文字数では測りません。読者またはAIが、目的を誤らず、根拠を辿り、境界を守り、正しい次の行動を選べるかで検証します。
"""
    return header + "\n".join(toc) + "\n\n" + "\n".join(sections) + footer


def build_readme(
    config: ProjectConfig,
    blocks: Iterable[SemanticBlock],
    *,
    output: Path,
    manifest_output: Path | None = None,
) -> str:
    block_list = list(blocks)
    rendered = render_readme(config, block_list)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    if manifest_output:
        manifest_output.parent.mkdir(parents=True, exist_ok=True)
        manifest_output.write_text(
            json.dumps(snapshot_data(block_list), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return rendered
