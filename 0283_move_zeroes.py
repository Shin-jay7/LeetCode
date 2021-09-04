from __future__ import annotations
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)
            

test = Solution()
test.moveZeroes([0,1,0,3,12]) # [1,3,12,0,0]

test = Solution()
test.moveZeroes([0]) # [0]
