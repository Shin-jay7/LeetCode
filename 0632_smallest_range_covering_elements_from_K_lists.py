from __future__ import annotations
from typing import List
from heapq import heapify, heappop, heappush
from collections import defaultdict


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        ans = -1e9, 1e9
        queue = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(queue)
        right = max(row[0] for row in nums)
        while queue:
            left, i, j = heappop(queue)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            val = nums[i][j+1]
            right = max(right, val)
            heappush(queue, (val, i, j+1))
