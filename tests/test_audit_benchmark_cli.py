from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from meaning_first_readme.audit import audit_repository, render_audit_markdown
from meaning_first_readme.benchmark import render_benchmark_markdown, run_benchmark
from tests.helpers import block, config


class AuditBenchmarkCliTests(unittest.TestCase):
    def healthy_blocks(self):
        return [
            block("purpose.test", priority=100),
            block("scope.test", kind="scope", depends_on=("purpose.test",)),
            block(
                "decision.test",
                kind="decision",
                depends_on=("purpose.test",),
                rationale="A documented reason.",
            ),
            block(
                "procedure.test",
                kind="procedure",
                depends_on=("purpose.test",),
                acceptance=("result is observable",),
            ),
        ]

    def test_audit_passes_healthy_repository(self):
        cfg = config(required_kinds=("purpose",), required_blocks=("purpose.test",))
        report = audit_repository(cfg, self.healthy_blocks())
        self.assertTrue(report.passed)

    def test_audit_reports_orphan(self):
        cfg = config(required_kinds=("purpose",), required_blocks=("purpose.test",))
        orphan = block("example.orphan", kind="example")
        report = audit_repository(cfg, self.healthy_blocks() + [orphan])
        self.assertFalse(report.passed)
        self.assertIn("example.orphan", report.data["dimensions"]["connectivity"]["orphan_blocks"])

    def test_audit_markdown_has_gates(self):
        cfg = config(required_kinds=("purpose",), required_blocks=("purpose.test",))
        rendered = render_audit_markdown(audit_repository(cfg, self.healthy_blocks()))
        self.assertIn("Quality gates", rendered)
        self.assertIn("no_validation_errors", rendered)

    def test_benchmark_passes_expected_retrieval(self):
        cfg = config(
            required_kinds=("purpose",),
            required_blocks=("purpose.test",),
            mandatory_context_blocks=("purpose.test",),
            benchmark_min_precision=0.1,
        )
        blocks = self.healthy_blocks()
        cases = [{"name": "release", "query": "procedure observable result", "expected": ["procedure.test"], "budget": 4000}]
        report = run_benchmark(cfg, blocks, cases)
        self.assertTrue(report.passed)
        self.assertEqual(report.cases[0].recall, 1.0)

    def test_benchmark_fails_missing_expected(self):
        cfg = config(
            required_kinds=("purpose",),
            required_blocks=("purpose.test",),
            mandatory_context_blocks=("purpose.test",),
            benchmark_min_precision=0.0,
        )
        cases = [{"name": "missing", "query": "unrelated", "expected": ["unknown.block"], "budget": 1000}]
        report = run_benchmark(cfg, self.healthy_blocks(), cases)
        self.assertFalse(report.passed)

    def test_benchmark_markdown_has_case(self):
        cfg = config(
            required_kinds=("purpose",),
            required_blocks=("purpose.test",),
            mandatory_context_blocks=("purpose.test",),
            benchmark_min_precision=0.0,
        )
        report = run_benchmark(cfg, self.healthy_blocks(), [{"name": "purpose", "query": "purpose", "expected": ["purpose.test"], "budget": 2000}])
        self.assertIn("purpose", render_benchmark_markdown(report))

    def test_cli_doctor_on_repository(self):
        root = Path(__file__).resolve().parents[1]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(root / "src")
        result = subprocess.run(
            [sys.executable, "-m", "meaning_first_readme", "doctor"],
            cwd=root,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("validation=PASS", result.stdout)

    def test_cli_validate_json(self):
        root = Path(__file__).resolve().parents[1]
        env = os.environ.copy()
        env["PYTHONPATH"] = str(root / "src")
        result = subprocess.run(
            [sys.executable, "-m", "meaning_first_readme", "validate", "--json"],
            cwd=root,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["passed"])


if __name__ == "__main__":
    unittest.main()
