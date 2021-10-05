from __future__ import annotations
from typing import List
from functools import cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            return min(dp(i-coin) + 1 for coin in coins)

        return dp(amount) if dp(amount) != float("inf") else -1
