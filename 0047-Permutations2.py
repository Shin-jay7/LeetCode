from __future__ import annotations
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def btrack(perm, counter):
            if len(perm)==len(nums):
                ans.append(perm[:])
                # https://stackoverflow.com/questions/32448414/what-does-colon-at-assignment-for-list-do-in-python
            for i in counter:
                if counter[i] > 0:
                    perm.append(i)
                    counter[i] -= 1
                    btrack(perm, counter)
                    perm.pop()
                    counter[i] += 1

        btrack([], Counter(nums))

        # print(ans)
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
