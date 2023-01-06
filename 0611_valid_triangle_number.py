from __future__ import annotations
from typing import List
from itertools import combinations


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        for a, b, c in combinations(nums, 3):
            if a < b+c and a < b+c and c < a+b:
                ans += 1

        return ans


test = Solution()
test.triangleNumber([2,2,3,4])
