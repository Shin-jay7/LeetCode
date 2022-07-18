from __future__ import annotations
from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ctr = Counter(nums)
        return sum(
             k > 0 and i + k in ctr or k == 0 and ctr[i] > 1 for i in ctr
            )


# Time limit exceeded
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = set()
        if k == 0:
            for a, b in combinations(nums, 2):
                if a == b:
                    ans.add((a, b))
        else:
            for a, b in combinations(set(nums), 2):
                if abs(a - b) == k:
                    ans.add((a, b))
        # print(len(ans))
        return len(ans)


test = Solution()
test.findPairs([3,1,4,1,5], 2) # 2

test = Solution()
test.findPairs([1,3,1,5,4], 0) # 1

test = Solution()
test.findPairs([1,3,1,1,2,2,5,4], 0) # 2

test = Solution()
test.findPairs([1,2,4,4,3,3,0,9,2,3], 3) # 2
