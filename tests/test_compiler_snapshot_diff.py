from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from meaning_first_readme.compiler import build_readme, render_readme
from meaning_first_readme.diff import compare_snapshots, render_diff_markdown
from meaning_first_readme.snapshot import snapshot_data, write_snapshot
from tests.helpers import block, config


class CompilerSnapshotDiffTests(unittest.TestCase):
    def blocks(self):
        return [
            block(),
            block("scope.test", kind="scope", title="Scope", summary="The supported scope is clearly declared.", depends_on=("purpose.test",), order=20),
        ]

    def test_render_contains_project_and_manifest(self):
        text = render_readme(config(), self.blocks())
        self.assertIn("# Test Project", text)
        self.assertIn("mfr:manifest", text)
        self.assertIn("機械可読マニフェスト", text)

    def test_render_contains_block_markers(self):
        text = render_readme(config(), self.blocks())
        self.assertIn("mfr:block", text)
        self.assertIn("purpose.test", text)

    def test_render_is_deterministic(self):
        self.assertEqual(render_readme(config(), self.blocks()), render_readme(config(), list(reversed(self.blocks()))))

    def test_build_writes_readme_and_manifest(self):
        directory = Path(tempfile.mkdtemp())
        output = directory / "README.md"
        manifest = directory / "manifest.json"
        build_readme(config(), self.blocks(), output=output, manifest_output=manifest)
        self.assertTrue(output.exists())
        self.assertTrue(manifest.exists())
        self.assertIn("repository_digest", manifest.read_text(encoding="utf-8"))

    def test_snapshot_digest_changes_with_body(self):
        before = snapshot_data(self.blocks())
        changed = [replace(self.blocks()[0], body="Changed body with a different semantic claim."), self.blocks()[1]]
        after = snapshot_data(changed)
        self.assertNotEqual(before["repository_digest"], after["repository_digest"])


    def test_snapshot_is_independent_of_source_path(self):
        first = replace(self.blocks()[0], path=Path("/one/location/block.md"))
        second = replace(self.blocks()[0], path=Path("/another/location/block.md"))
        self.assertEqual(snapshot_data([first])["repository_digest"], snapshot_data([second])["repository_digest"])

    def test_write_snapshot(self):
        path = Path(tempfile.mkdtemp()) / "snapshot.json"
        data = write_snapshot(path, self.blocks())
        self.assertTrue(path.exists())
        self.assertEqual(data["schema_version"], 1)

    def test_diff_added_removed_modified(self):
        left = snapshot_data(self.blocks())
        right_blocks = [replace(self.blocks()[0], title="New title"), block("constraint.new", kind="constraint")]
        right = snapshot_data(right_blocks)
        diff = compare_snapshots(left, right)
        self.assertIn("constraint.new", diff.added)
        self.assertIn("scope.test", diff.removed)
        self.assertIn("purpose.test", diff.modified)

    def test_diff_markdown(self):
        left = snapshot_data(self.blocks())
        right = snapshot_data([replace(self.blocks()[0], title="New title"), self.blocks()[1]])
        rendered = render_diff_markdown(compare_snapshots(left, right))
        self.assertIn("Semantic Diff", rendered)
        self.assertIn("purpose.test", rendered)


if __name__ == "__main__":
    unittest.main()
