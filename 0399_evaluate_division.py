from __future__ import annotations
from typing import List
from collections import defaultdict, deque
from itertools import permutations


class Solution:
    def calcEquation(
            self,
            equations: List[List[str]],
            values: List[float],
            queries: List[List[str]]
        ):
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def search(a: str, b: str) -> float:
            if a not in graph or b not in graph:
                return -1.0

            if a == b:
                return 1.0

            used, queue = {a}, deque([(a, 1.0)])
            while queue:
                currNode, currVal = queue.popleft()
                for nextNode, nextVal in graph[currNode].items():
                    if nextNode in used:
                        continue
                    totalVal = currVal * nextVal
                    if nextNode == b:
                        graph[a][b] = totalVal
                        graph[b][a] = 1 / totalVal
                        return totalVal
                    used.add(nextNode)
                    queue.append((nextNode, totalVal))

            return -1.0

        return [search(a, b) for a, b in queries]


# Floyd-Warshall
# a/b = k is like a graph edge a->b
# (a/b)*(b/c)*(c/d) is like the path a->b->c->d
class Solution:
    def calcEquation(
            self,
            equations: List[List[str]],
            values: List[float],
            queries: List[List[str]]
        ):
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][a] = graph[b][b] = 1.0
            graph[a][b] = val
            graph[b][a] = 1 / val
        for c, a, b in permutations(graph, 3):
            if c in graph[a] and b in graph[c]:
                graph[a][b] = graph[a][c] * graph[c][b]

        return [graph[a].get(b, -1.0) for a, b in queries]
