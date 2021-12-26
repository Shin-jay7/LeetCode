from __future__ import annotations
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        cnt = 1
        nums.sort(reverse=True)
        for i in range(1, len(nums)):
            if cnt == 3:
                return nums[i-1]
            elif nums[i] != nums[i-1]:
                cnt += 1

        return nums[-1] if cnt == 3 else nums[0]
