from __future__ import annotations
from functools import cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cost = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                cost[lo][hi] =\
                    min(pick + max(cost[lo][pick-1], cost[pick+1][hi])
                        for pick in range(lo, hi))

        return cost[1][n]


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def cost(lo, hi):
            return min([pick + max(cost(lo, pick-1), cost(pick+1, hi))
                       for pick in range(lo, hi+1)]) if lo < hi else 0

        return cost(1, n)

