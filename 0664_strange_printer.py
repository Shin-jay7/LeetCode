from __future__ import annotations
from itertools import groupby


class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        # Let dp(i, j) be the number of turns needed to print s[i:j+1]
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) not in memo:
                ans = dp(i, j-1) + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        ans = min(ans, dp(i, k-1) + dp(k, j-1))
                memo[(i, j)] = ans
            return memo[(i, j)]

        s = [key for key, group in groupby(s)]
        return dp(0, len(s)-1)
