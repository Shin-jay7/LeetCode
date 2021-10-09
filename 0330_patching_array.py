from __future__ import annotations
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach, patches, idx = 0, 0, 0
        while reach < n:
            if idx < len(nums) and nums[idx] <= reach + 1:
                reach += nums[idx]
                idx += 1
            else:
                patches += 1
                reach = 2*reach + 1

        return patches
