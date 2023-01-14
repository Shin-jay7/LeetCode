from __future__ import annotations
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        size, _max = len(nums), float('-inf')
        if not nums:
            return 0
        if k >= size:
            return sum(nums) / size
        for i in range(size-k+1):
            _max = max(_max, sum(nums[i:i+k]) / k)
        print(_max)
        return _max


test = Solution()
test.findMaxAverage([0,1,1,3,3], 4)  # 2.00000
