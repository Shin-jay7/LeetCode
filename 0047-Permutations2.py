from __future__ import annotations
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for l in permutations(nums):
            l = list(l)
            if not l in ans:
                ans.append(l)

        return ans




test = Solution()
test.permuteUnique([1,1,2])
"""
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
