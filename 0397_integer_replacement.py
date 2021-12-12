from __future__ import annotations
from functools import cache


class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if not n % 2:
            return 1 + self.integerReplacement(n//2)

        return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
