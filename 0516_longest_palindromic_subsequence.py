from __future__ import annotations
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dp(i+1, j-1) + 2
            return max(dp(i, j-1), dp(i+1, j))

        return dp(0, len(s)-1)


