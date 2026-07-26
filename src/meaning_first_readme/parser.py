from __future__ import annotations

import tomllib
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable

from .errors import ParseError
from .model import SemanticBlock, ProjectConfig

FRONT_MATTER = "+++"
KNOWN_FIELDS = {
    "id",
    "kind",
    "title",
    "summary",
    "order",
    "priority",
    "audience",
    "tags",
    "status",
    "trust",
    "depends_on",
    "evidence",
    "supports",
    "claims",
    "negates",
    "acceptance",
    "rationale",
    "owner",
    "source",
    "updated",
    "expires",
    "volatile",
}


def _as_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,)
    if isinstance(value, (list, tuple)):
        return tuple(str(item) for item in value)
    raise TypeError(f"expected string or array, got {type(value).__name__}")


def _as_date(value: Any) -> date | None:
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError as exc:
            raise TypeError(f"invalid ISO date: {value}") from exc
    raise TypeError(f"expected ISO date, got {type(value).__name__}")


def parse_block(path: Path) -> SemanticBlock:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ParseError(f"{path}: cannot read: {exc}") from exc

    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONT_MATTER:
        raise ParseError(f"{path}: first line must be {FRONT_MATTER!r}")

    try:
        end = next(
            index for index, line in enumerate(lines[1:], start=1) if line.strip() == FRONT_MATTER
        )
    except StopIteration as exc:
        raise ParseError(f"{path}: front matter is not closed") from exc

    front = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :]).strip()
    try:
        metadata = tomllib.loads(front)
    except tomllib.TOMLDecodeError as exc:
        raise ParseError(f"{path}: invalid TOML front matter: {exc}") from exc

    missing = [name for name in ("id", "kind", "title", "summary") if not metadata.get(name)]
    if missing:
        raise ParseError(f"{path}: missing required fields: {', '.join(missing)}")
    if not body:
        raise ParseError(f"{path}: block body must not be empty")

    try:
        return SemanticBlock(
            id=str(metadata["id"]),
            kind=str(metadata["kind"]),
            title=str(metadata["title"]),
            summary=str(metadata["summary"]),
            body=body,
            order=int(metadata.get("order", 1000)),
            priority=int(metadata.get("priority", 50)),
            audience=_as_tuple(metadata.get("audience", "both")),
            tags=_as_tuple(metadata.get("tags")),
            status=str(metadata.get("status", "active")),
            trust=str(metadata.get("trust", "reviewed")),
            depends_on=_as_tuple(metadata.get("depends_on")),
            evidence=_as_tuple(metadata.get("evidence")),
            supports=_as_tuple(metadata.get("supports")),
            claims=_as_tuple(metadata.get("claims")),
            negates=_as_tuple(metadata.get("negates")),
            acceptance=_as_tuple(metadata.get("acceptance")),
            rationale=str(metadata.get("rationale", "")),
            owner=str(metadata.get("owner", "")),
            source=str(metadata.get("source", "")),
            updated=_as_date(metadata.get("updated")),
            expires=_as_date(metadata.get("expires")),
            volatile=bool(metadata.get("volatile", False)),
            path=path,
            extra={key: value for key, value in metadata.items() if key not in KNOWN_FIELDS},
        )
    except (TypeError, ValueError) as exc:
        raise ParseError(f"{path}: invalid metadata: {exc}") from exc


def discover_blocks(content_dir: Path) -> list[SemanticBlock]:
    if not content_dir.exists():
        raise ParseError(f"content directory does not exist: {content_dir}")
    paths = sorted(path for path in content_dir.rglob("*.md") if path.is_file())
    if not paths:
        raise ParseError(f"no .md blocks found below {content_dir}")
    return [parse_block(path) for path in paths]


def load_project(path: Path) -> ProjectConfig:
    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ParseError(f"{path}: cannot read project config: {exc}") from exc
    except tomllib.TOMLDecodeError as exc:
        raise ParseError(f"{path}: invalid TOML: {exc}") from exc
    return ProjectConfig.from_mapping(raw, root=path.parent.parent if path.parent.name == "content" else path.parent)


def load_repository(project_file: Path) -> tuple[ProjectConfig, list[SemanticBlock]]:
    config = load_project(project_file.resolve())
    return config, discover_blocks(config.content_dir)


def index_blocks(blocks: Iterable[SemanticBlock]) -> dict[str, SemanticBlock]:
    index: dict[str, SemanticBlock] = {}
    for block in blocks:
        if block.id in index:
            first = index[block.id].path or "<memory>"
            second = block.path or "<memory>"
            raise ParseError(f"duplicate block id {block.id!r}: {first} and {second}")
        index[block.id] = block
    return index
