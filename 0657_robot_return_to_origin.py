from __future__ import annotations
from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("R") == moves.count("L") and\
               moves.count("U") == moves.count("D")


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        return c("R") == c("L") and c("U") == c("D")
