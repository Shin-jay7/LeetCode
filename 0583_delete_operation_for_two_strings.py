from __future__ import annotations
from collections import Counter


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if i == len(word1) or j == len(word2):
                    ans = len(word1) + len(word2) - i - j
                elif word1[i] == word2[j]:
                    ans = dp(i+1, j+1)
                else:
                    ans = 1 + min(dp(i+1, j), dp(i, j+1))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]

        for i in range(len1):
            dp[i][-1] = len1-i
        for j in range(len2):
            dp[-1][j] = len2-j

        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
