from __future__ import annotations
from typing import List


# https://leetcode.com/problems/ones-and-zeroes/discuss/1138695/JS-Python-Java-C%2B%2B-or-Easy-DP-Knapsack-Solution-w-Explanation
class Solution:
    def findMaxForm(self, str: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in str:
            zeros = s.count("0")
            ones = len(s) - zeros
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[m][n]


# https://leetcode.com/problems/ones-and-zeroes/discuss/814077/Dedicated-to-Beginners
class Solution:
    def findMaxForm(self, str: List[str], m: int, n: int) -> int:
        L = len(str)
        dp = [[[-1 for col in range(n+1)] for col in range(m+1)] for row in range(L)]

        def knapsack(L, zero, one):
            if L < 0 or (zero == 0 and one == 0):
                return 0
            cnt0 = str[L].count("0")
            cnt1 = str[L].count("1")
            if dp[L][zero][one] != -1:
                return dp[L][zero][one]
            if cnt0 > zero or cnt1 > one:
                dp[L][zero][one] = knapsack(L-1, zero, one)
                return dp[L][zero][one]
            else:
                include = 1+knapsack(L-1, zero-cnt0, one-cnt1)
                exclude = knapsack(L-1, zero, one)
                dp[L][zero][one] = max(include, exclude)
                return dp[L][zero][one]

        return knapsack(L-1, m, n)
