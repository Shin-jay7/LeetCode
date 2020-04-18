from __future__ import annotations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
          perm = []
          for l in ans:
            for i in range(len(l)+1):
              perm.append(l[:i]+[n]+l[i:])
          ans = perm

        return ans


test = Solution()
test.permute([1,2,3])
"""
  [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
