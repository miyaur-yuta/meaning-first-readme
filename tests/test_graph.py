from __future__ import annotations

import unittest

from meaning_first_readme.graph import MeaningGraph
from tests.helpers import block


class GraphTests(unittest.TestCase):
    def test_missing_references(self):
        graph = MeaningGraph([block(depends_on=("missing.x",))])
        self.assertEqual(graph.missing_references()[0][2], "missing.x")

    def test_dependency_closure(self):
        blocks = [
            block("purpose.a"),
            block("scope.b", kind="scope", depends_on=("purpose.a",)),
            block("decision.c", kind="decision", depends_on=("scope.b",), rationale="because"),
        ]
        graph = MeaningGraph(blocks)
        self.assertEqual(graph.dependency_closure({"decision.c"}), {"purpose.a", "scope.b", "decision.c"})

    def test_detects_cycle(self):
        graph = MeaningGraph([
            block("purpose.a", depends_on=("scope.b",)),
            block("scope.b", kind="scope", depends_on=("purpose.a",)),
        ])
        cycles = graph.cycles()
        self.assertEqual(len(cycles), 1)
        self.assertEqual(cycles[0].path[0], cycles[0].path[-1])

    def test_no_cycle(self):
        graph = MeaningGraph([block("purpose.a"), block("scope.b", kind="scope", depends_on=("purpose.a",))])
        self.assertEqual(graph.cycles(), [])

    def test_topological_dependencies_first(self):
        graph = MeaningGraph([
            block("purpose.a"),
            block("scope.b", kind="scope", depends_on=("purpose.a",)),
        ])
        result = graph.topological()
        self.assertLess(result.index("purpose.a"), result.index("scope.b"))

    def test_topological_raises_on_cycle(self):
        graph = MeaningGraph([
            block("purpose.a", depends_on=("scope.b",)),
            block("scope.b", kind="scope", depends_on=("purpose.a",)),
        ])
        with self.assertRaises(ValueError):
            graph.topological()

    def test_reachable_uses_both_directions(self):
        graph = MeaningGraph([
            block("purpose.a"),
            block("scope.b", kind="scope", depends_on=("purpose.a",)),
            block("decision.c", kind="decision", depends_on=("scope.b",), rationale="x"),
        ])
        self.assertEqual(graph.reachable_from({"purpose.a"}), {"purpose.a", "scope.b", "decision.c"})

    def test_explain_includes_dependencies_and_users(self):
        graph = MeaningGraph([
            block("purpose.a"),
            block("scope.b", kind="scope", depends_on=("purpose.a",)),
        ])
        explanation = graph.explain("purpose.a")
        self.assertEqual(explanation["used_by"][0]["id"], "scope.b")


if __name__ == "__main__":
    unittest.main()
