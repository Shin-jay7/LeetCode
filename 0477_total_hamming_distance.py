from __future__ import annotations
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            ones = zeros = 0
            for n in nums:
                ones += (n >> i) & 1
                zeros += not (n >> i) & 1
            ans += ones * zeros

        return ans
