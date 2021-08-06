from __future__ import annotations


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_square_len = 0
        dp = [0] * (cols+1)
        prev = 0

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                    max_square_len = max(max_square_len, dp[j])
                else:
                    dp[j] = 0
                prev = tmp

        return max_square_len ** 2
