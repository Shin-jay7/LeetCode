from __future__ import annotations
from typing import List


# https://leetcode.com/problems/redundant-connection-ii/solutions/254733/python-union-find-clear-logic/?orderBy=most_votes
class DisjointSet:  # UnionFind
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, u: int, v: int) -> bool:
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        self.parent[u] = self.parent[v]
        return True


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) \
     -> List[int]:
        # root (no cycle) & one parent <- OK!
        # root (no cycle) & two parents
        # no root (cycle) & one parent
        # no root (cycle) & two parents
        cand1, cand2, parent_child = None, None, {}
        for u, v in edges:
            if v in parent_child:
                cand1, cand2 = parent_child[v], [u, v]
                break
            parent_child[v] = [u, v]
        ds = DisjointSet(len(edges))
        for u, v in edges:
            if [u, v] == cand2:
                continue
            if not ds.union(u-1, v-1):
                if cand1:
                    return cand1
                return [u, v]
        return cand2
