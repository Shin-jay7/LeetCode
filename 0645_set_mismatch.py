from __future__ import annotations
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        _sum, a, b = n * (n+1) // 2, sum(nums), sum(set(nums))
        return [a-b, _sum-b]


test = Solution()
test.findErrorNums([1,2,2,4])  # [2,3]

test = Solution()
test.findErrorNums([3,2,3,4,6,5])  # [3,1]
