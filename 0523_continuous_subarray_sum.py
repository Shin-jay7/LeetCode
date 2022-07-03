from __future__ import annotations
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length < 2:
            return False

        for i in range(length):
            for j in range(i+1, length):
                if sum(nums[i:j+1]) % k == 0:
                    return True

        return False
