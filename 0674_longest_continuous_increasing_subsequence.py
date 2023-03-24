from __future__ import annotations
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt, ans = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1]+1
        return max(dp)


test = Solution()
test.findLengthOfLCIS([1,3,5,4,7]) # 3

test = Solution()
test.findLengthOfLCIS([2,2,2,2,2]) # 1
