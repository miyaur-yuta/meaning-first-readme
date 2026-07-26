from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class SemanticDiff:
    added: tuple[str, ...]
    removed: tuple[str, ...]
    modified: dict[str, dict[str, object]]

    @property
    def changed(self) -> bool:
        return bool(self.added or self.removed or self.modified)

    def to_dict(self) -> dict[str, object]:
        return {
            "changed": self.changed,
            "added": list(self.added),
            "removed": list(self.removed),
            "modified": self.modified,
        }


def _index(snapshot: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {str(block["id"]): block for block in snapshot.get("blocks", [])}


def compare_snapshots(left: Mapping[str, Any], right: Mapping[str, Any]) -> SemanticDiff:
    old = _index(left)
    new = _index(right)
    added = tuple(sorted(set(new) - set(old)))
    removed = tuple(sorted(set(old) - set(new)))
    modified: dict[str, dict[str, object]] = {}
    ignored = {"digest", "path"}
    for identifier in sorted(set(old) & set(new)):
        before = old[identifier]
        after = new[identifier]
        if before.get("digest") == after.get("digest"):
            continue
        changes: dict[str, object] = {}
        for field in sorted((set(before) | set(after)) - ignored):
            if before.get(field) != after.get(field):
                changes[field] = {"before": before.get(field), "after": after.get(field)}
        if changes:
            modified[identifier] = changes
    return SemanticDiff(added=added, removed=removed, modified=modified)


def render_diff_markdown(diff: SemanticDiff) -> str:
    lines = ["# Semantic Diff", "", f"**Changed:** {'yes' if diff.changed else 'no'}", ""]
    lines.extend(["## Added", ""])
    lines.extend(f"- `{identifier}`" for identifier in diff.added)
    if not diff.added:
        lines.append("- None")
    lines.extend(["", "## Removed", ""])
    lines.extend(f"- `{identifier}`" for identifier in diff.removed)
    if not diff.removed:
        lines.append("- None")
    lines.extend(["", "## Modified", ""])
    if not diff.modified:
        lines.append("- None")
    for identifier, fields in diff.modified.items():
        lines.append(f"### `{identifier}`")
        lines.append("")
        for field, values in fields.items():
            lines.append(f"- **{field}**")
            lines.append(f"  - before: `{values['before']}`")
            lines.append(f"  - after: `{values['after']}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
