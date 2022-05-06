from __future__ import annotations
from functools import lru_cache
from typing import List


# Keep track of the difference between player1 and player2.
# Return True if the difference >= 0
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        @lru_cache(None)
        def recursive(l_idx, r_idx):
            if l_idx == r_idx:
                return nums[l_idx]
            return max(nums[l_idx] - recursive(l_idx+1, r_idx),
                       nums[r_idx] - recursive(l_idx, r_idx-1))

        return True if recursive(0, n-1) >= 0 else False


# dp[i][j] is the margin of the score when it's current player's turn and
# the array left are nums[i]..nums[j] inclusively.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # d[i][j]  Effective score to pick when facing nums[i...j]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for s in range(n):
            for i in range(n-s):
                j = i + s
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j])

        return dp[0][-1] >= 0


# the dp updates the hill diagnal which depends only on previous hill diagal,
# so it could be turned to a 1-D DP.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n, dp = len(nums), nums[:]
        for s in range(1, n):
            new_dp = [0] * n
            for j in range(s, n):
                i = j - s
                new_dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
            dp = new_dp

        return dp[-1] >= 0
        