from __future__ import annotations
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]

        while len(dp) <= n:
            x, y = len(dp), float('inf')
            for i in range(1, int(sqrt(x))+1):
                idx = x - i*i
                if dp[idx] + 1 < y:
                    y = dp[idx] + 1
            dp.append(y)
            # print(dp)

        return dp[n]


test = Solution()
test.numSquares(13) # 2
