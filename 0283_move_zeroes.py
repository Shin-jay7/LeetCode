from __future__ import annotations
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


test = Solution()
test.moveZeroes([0,1,0,3,12]) # [1,3,12,0,0]

test = Solution()
test.moveZeroes([0]) # [0]
