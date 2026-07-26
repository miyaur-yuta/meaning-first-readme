from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from meaning_first_readme.errors import ParseError
from meaning_first_readme.parser import discover_blocks, load_project, parse_block


class ParserTests(unittest.TestCase):
    def write(self, text: str, name: str = "block.md") -> Path:
        directory = Path(tempfile.mkdtemp())
        path = directory / name
        path.write_text(text, encoding="utf-8")
        return path

    def valid_text(self) -> str:
        return '''+++
id = "purpose.demo"
kind = "purpose"
title = "Demo"
summary = "A complete and useful summary."
priority = 90
audience = ["human", "ai"]
updated = "2026-07-26"
+++
Body text.
'''

    def test_parse_valid_block(self):
        parsed = parse_block(self.write(self.valid_text()))
        self.assertEqual(parsed.id, "purpose.demo")
        self.assertEqual(parsed.priority, 90)
        self.assertEqual(parsed.audience, ("human", "ai"))
        self.assertEqual(parsed.updated.isoformat(), "2026-07-26")
        self.assertEqual(parsed.body, "Body text.")

    def test_requires_opening_delimiter(self):
        with self.assertRaises(ParseError):
            parse_block(self.write("id = 'x'"))

    def test_requires_closing_delimiter(self):
        with self.assertRaises(ParseError):
            parse_block(self.write("+++\nid='purpose.x'"))

    def test_rejects_invalid_toml(self):
        with self.assertRaises(ParseError):
            parse_block(self.write("+++\nid = [\n+++\nbody"))

    def test_requires_core_fields(self):
        text = "+++\nid='purpose.x'\nkind='purpose'\n+++\nbody"
        with self.assertRaises(ParseError) as captured:
            parse_block(self.write(text))
        self.assertIn("missing required fields", str(captured.exception))

    def test_requires_nonempty_body(self):
        text = "+++\nid='purpose.x'\nkind='purpose'\ntitle='x'\nsummary='long enough summary'\n+++\n"
        with self.assertRaises(ParseError):
            parse_block(self.write(text))

    def test_preserves_unknown_metadata(self):
        text = self.valid_text().replace("priority = 90", "priority = 90\ncustom = 'value'")
        parsed = parse_block(self.write(text))
        self.assertEqual(parsed.extra["custom"], "value")

    def test_discover_blocks_is_sorted(self):
        directory = Path(tempfile.mkdtemp())
        (directory / "b.md").write_text(self.valid_text().replace("purpose.demo", "purpose.b"), encoding="utf-8")
        (directory / "a.md").write_text(self.valid_text().replace("purpose.demo", "purpose.a"), encoding="utf-8")
        blocks = discover_blocks(directory)
        self.assertEqual([item.id for item in blocks], ["purpose.a", "purpose.b"])

    def test_discover_requires_files(self):
        with self.assertRaises(ParseError):
            discover_blocks(Path(tempfile.mkdtemp()))

    def test_load_project_resolves_content_directory(self):
        root = Path(tempfile.mkdtemp())
        content = root / "content"
        content.mkdir()
        project = content / "project.toml"
        project.write_text("[project]\nname='X'\ncontent_dir='content/blocks'\n", encoding="utf-8")
        loaded = load_project(project)
        self.assertEqual(loaded.name, "X")
        self.assertEqual(loaded.content_dir, (root / "content/blocks").resolve())


if __name__ == "__main__":
    unittest.main()
