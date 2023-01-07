from __future__ import annotations
from typing import List
from heapq import nlargest, nsmallest


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        small, large = nsmallest(2, nums), nlargest(3, nums)
        return max(
             small[0] * small[1] * large[0], large[0] * large[1] * large[2]
            )
