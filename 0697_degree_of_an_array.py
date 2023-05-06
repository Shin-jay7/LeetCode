from __future__ import annotations
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count, ans, degree = {}, {}, 0, 0
        for idx, num in enumerate(nums):
            first.setdefault(num, idx)
            count[num] = count.get(num, 0) + 1
            if count[num] > degree:
                degree = count[num]
                ans = idx - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, idx - first[num] + 1)
        return ans
