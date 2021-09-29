from __future__ import annotations
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i][j] in here means, the maximum coins we get after 
        # we burst all the balloons between i and j 
        nums, n = [1]+nums+[1], len(nums)+2
        dp = [[0]*n for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                dp[i][j] =\
                    max(dp[i][k]+nums[i]*nums[k]*nums[j]+dp[k][j] for k in range(i+1, j))

        return dp[0][n-1]
