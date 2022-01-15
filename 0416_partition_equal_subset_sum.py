from __future__ import annotations
from typing import List
from functools import cache


https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624391/Python-DP-and-DFS-Solutions-Easy-to-understand-with-Explanation
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        dp = set([0])
        for num in nums:
            dp.update([v+num for v in dp if v+num <= s//2])
        return s//2 in dp


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length, s = len(nums), sum(nums)

        @cache
        def dfs(curr: int, idx: int) -> bool:
            if idx == length:
                return curr == s//2
            elif curr+nums[idx] == s//2 or\
                (curr+nums[idx] < s//2 and dfs(curr+nums[idx], idx+1)):
                return True
            return dfs(curr, idx+1)

        return False if s % 2 else dfs(0, 0)



test = Solution()
test.canPartition([1,5,11,5]) # True

test = Solution()
test.canPartition([1,2,3,5]) # False
