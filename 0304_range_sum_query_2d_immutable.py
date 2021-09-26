from __future__ import annotations
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        dp = self.dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + matrix[i][j] - dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp
        return dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1]
