from __future__ import annotations
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[target]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target):
            if not dp[i]:
                continue
            for num in nums:
                if num + i <= target:
                    dp[i+num] += dp[i]

        return dp[target]

