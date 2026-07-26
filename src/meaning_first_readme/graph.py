from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterable

from .model import SemanticBlock


@dataclass(frozen=True, slots=True)
class Cycle:
    path: tuple[str, ...]


class MeaningGraph:
    def __init__(self, blocks: Iterable[SemanticBlock]):
        self.blocks = {block.id: block for block in blocks}
        self.dependencies: dict[str, set[str]] = {
            block.id: set(block.depends_on) | set(block.evidence) for block in self.blocks.values()
        }
        self.reverse: dict[str, set[str]] = defaultdict(set)
        for source, targets in self.dependencies.items():
            for target in targets:
                self.reverse[target].add(source)

    def missing_references(self) -> list[tuple[str, str, str]]:
        missing: list[tuple[str, str, str]] = []
        for block in self.blocks.values():
            for target in block.depends_on:
                if target not in self.blocks:
                    missing.append((block.id, "depends_on", target))
            for target in block.evidence:
                if target not in self.blocks:
                    missing.append((block.id, "evidence", target))
            for target in block.supports:
                if target not in self.blocks:
                    missing.append((block.id, "supports", target))
        return sorted(missing)

    def cycles(self) -> list[Cycle]:
        color: dict[str, int] = {node: 0 for node in self.blocks}
        stack: list[str] = []
        found: set[tuple[str, ...]] = set()

        def visit(node: str) -> None:
            color[node] = 1
            stack.append(node)
            for target in sorted(self.dependencies.get(node, ())):
                if target not in self.blocks:
                    continue
                if color[target] == 0:
                    visit(target)
                elif color[target] == 1:
                    start = stack.index(target)
                    cycle = stack[start:] + [target]
                    rotations = []
                    core = cycle[:-1]
                    for index in range(len(core)):
                        rotated = core[index:] + core[:index]
                        rotations.append(tuple(rotated + [rotated[0]]))
                    found.add(min(rotations))
            stack.pop()
            color[node] = 2

        for node in sorted(self.blocks):
            if color[node] == 0:
                visit(node)
        return [Cycle(path=value) for value in sorted(found)]

    def dependency_closure(self, identifiers: Iterable[str]) -> set[str]:
        selected = set(identifiers)
        queue = deque(selected)
        while queue:
            node = queue.popleft()
            for dependency in self.dependencies.get(node, ()):
                if dependency in self.blocks and dependency not in selected:
                    selected.add(dependency)
                    queue.append(dependency)
        return selected

    def reachable_from(self, roots: Iterable[str]) -> set[str]:
        seen = set(roots)
        queue = deque(seen)
        while queue:
            node = queue.popleft()
            neighbors = self.dependencies.get(node, set()) | self.reverse.get(node, set())
            for neighbor in neighbors:
                if neighbor in self.blocks and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return seen

    def topological(self) -> list[str]:
        indegree = {node: 0 for node in self.blocks}
        for source, targets in self.dependencies.items():
            indegree[source] = sum(1 for target in targets if target in self.blocks)
        queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
        result: list[str] = []
        reverse = self.reverse
        while queue:
            node = queue.popleft()
            result.append(node)
            for dependent in sorted(reverse.get(node, ())):
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        if len(result) != len(self.blocks):
            raise ValueError("graph contains a dependency cycle")
        return result

    def explain(self, identifier: str) -> dict[str, object]:
        if identifier not in self.blocks:
            raise KeyError(identifier)
        block = self.blocks[identifier]
        return {
            "block": block.to_dict(),
            "depends_on": [self.blocks[item].to_dict(include_body=False) for item in sorted(self.dependencies[identifier]) if item in self.blocks],
            "used_by": [self.blocks[item].to_dict(include_body=False) for item in sorted(self.reverse.get(identifier, ()))],
        }
