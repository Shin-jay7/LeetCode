from __future__ import annotations
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            perms = []
            for l in ans:
                for i in range((l+[n]).index(n)+1):
                    perms.append(l[:i]+[n]+l[i:])
            ans = perms

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
