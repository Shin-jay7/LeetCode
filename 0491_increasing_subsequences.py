from __future__ import annotations
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}
        for num in nums:
            tmp = {()}
            tmp |= {(num,)}
            for sub in subs:
                if sub and sub[-1] <= num:
                    tmp |= {sub+(num,)}
                    print(tmp)
            subs |= tmp
        return [sub for sub in subs if len(sub) >= 2]


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = {()}
        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]


test = Solution()
test.findSubsequences([4,6,7,7])
