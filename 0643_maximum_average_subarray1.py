from __future__ import annotations
from typing import List
from itertools import accumulate
from operator import sub


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = prefs = sum(nums[:k])
        for i in range(len(nums)-k):
            prefs += (nums[i+k] - nums[i])
            ans = max(ans, prefs)
        return ans / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = [0] + list(accumulate(nums))
        return max(map(sub, sums[k:], sums)) / k


test = Solution()
test.findMaxAverage([0,1,1,3,3], 4)  # 2.00000
