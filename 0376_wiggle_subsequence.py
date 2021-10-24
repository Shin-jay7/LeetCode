from __future__ import annotations
from typing import List
from functools import cache


# Define by dp(i, 1) the biggest length of wiggle subsequense, 
# which ends with element nums[i] and has and increasing status, 
# and dp(i, -1) is the biggest length of wiggle subsequence, 
# which ends with element nums[i] and has decreasing status.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i, s):
            if i == 0:
                return 1
            return dp(i-1, -s) + 1 if (nums[i]-nums[i-1])*s < 0 else dp(i-1, s)

        return max(dp(n-1, -1), dp(n-1, 1))
