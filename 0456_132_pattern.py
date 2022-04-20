from __future__ import annotations
from typing import List
from itertools import combinations


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for pair in combinations(nums, 3):
            if pair[0] < pair[2] < pair[1]:
                return True
        return False


test = Solution()
test.find132pattern([1,2,3,4])

test = Solution()
test.find132pattern([3,1,4,2])

test = Solution()
test.find132pattern([-1,3,2,0])
