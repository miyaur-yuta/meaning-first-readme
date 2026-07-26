from __future__ import annotations

import json
import unittest
from pathlib import Path

from meaning_first_readme.audit import audit_repository
from meaning_first_readme.benchmark import load_cases, run_benchmark
from meaning_first_readme.compiler import render_readme
from meaning_first_readme.parser import load_repository
from meaning_first_readme.validate import validate_repository


class RepositoryIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[1]
        cls.config, cls.blocks = load_repository(cls.root / "content/project.toml")

    def test_repository_has_substantial_block_set(self):
        self.assertGreaterEqual(len(self.blocks), 30)

    def test_repository_validation_passes_without_warnings(self):
        report = validate_repository(self.config, self.blocks)
        self.assertTrue(report.passed)
        self.assertEqual(report.warnings, ())

    def test_repository_audit_passes(self):
        self.assertTrue(audit_repository(self.config, self.blocks).passed)

    def test_repository_benchmark_passes(self):
        cases = load_cases(self.root / "benchmarks/tasks.json")
        report = run_benchmark(self.config, self.blocks, cases)
        self.assertTrue(report.passed)
        self.assertEqual(report.macro_recall, 1.0)
        self.assertGreaterEqual(report.macro_precision, self.config.benchmark_min_precision)

    def test_checked_in_readme_is_current(self):
        expected = render_readme(self.config, self.blocks)
        actual = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_manifest_contains_every_block(self):
        manifest = json.loads((self.root / "build/manifest.json").read_text(encoding="utf-8"))
        ids = {record["id"] for record in manifest["blocks"]}
        self.assertEqual(ids, {block.id for block in self.blocks})


if __name__ == "__main__":
    unittest.main()
