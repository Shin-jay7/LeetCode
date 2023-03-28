from __future__ import annotations
from collections import defaultdict


class MapSum:
    def __init__(self):
        self._map = {}

    def insert(self, key: str, val: int) -> None:
        self._map[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                ans += val
        return ans


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self._sum = 0


class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self._map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        dif = val - self._map[key]
        cur = self.root
        for cha in key:
            cur = cur.child[cha]
            cur._sum += dif
        self._map[key] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for cha in prefix:
            if cha not in cur.child:
                return 0
            cur = cur.child[cha]
        return cur._sum
