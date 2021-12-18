from __future__ import annotations
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set, seen, stack = set(stones), set(), [(0, 0)]
        while stack:
            stone, jump = stack.pop()
            for j in (jump-1, jump, jump+1):
                s = stone + j
                if j > 0 and s in stone_set and (s, j) not in seen:
                    if s == stones[-1]:
                        return True
                    stack.append((s, j))
            seen.add((stone, jump))

        return False
