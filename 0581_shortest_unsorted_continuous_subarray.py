from __future__ import annotations
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        small = nums[-1]
        for i in reversed(range(len(nums))):
            if nums[i] > small:
                start = i
            else:
                small = nums[i]

        end = 0
        big = nums[0]
        for i in range(len(nums)):
            if nums[i] < big:
                end = i
            else:
                big = nums[i]

        if start == end:
            return 0
        return end - start + 1


test = Solution()
test.findUnsortedSubarray([2,6,4,8,10,9,15])  # 5
