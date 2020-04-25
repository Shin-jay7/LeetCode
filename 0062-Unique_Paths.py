from __future__ import annotations


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n]*m

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
        # print(dp[m-1][n-1])


test = Solution()
test.uniquePaths(3, 2) # 3

test = Solution()
test.uniquePaths(7, 3) # 28
