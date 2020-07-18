from __future__ import annotations


# top-down approach calculating the answer from bottom-up
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]
        dp[m][n-1], dp[m-1][n],  = 1, 1 # Knight needs at least 1 HP remained at goal

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                minHP = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(minHP, 1) # HP must be positive. Otherwise knight dies.

        return dp[0][0]
