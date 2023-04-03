from __future__ import annotations
from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.already_connected = defaultdict(list)
        for edge in edges:
            self.visited = defaultdict(bool)
            x, y = edge[0], edge[1]
            if self.is_already_connected(x, y):
                return edge
            self.already_connected[x].append(y)
            self.already_connected[y].append(x)

    def is_already_connected(self, x, y):
        if x == y:
            return True
        for x_adjacent in self.already_connected[x]:
            if not self.visited[x_adjacent]:
                self.visited[x_adjacent] = True
                if self.is_already_connected(x_adjacent, y):
                    return True
        return False


class UnionFind:
    def __init__(self, n: int):
        self.parent = [_ for _ in range(n)]
        self.size = [1] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for u, v in edges:
            if not uf.union(u-1, v-1):
                return [u, v]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        node = ''.join(map(chr, range(1001)))
        for u, v in edges:
            if node[u] == node[v]:
                return [u, v]
            node = node.replace(node[u], node[v])
