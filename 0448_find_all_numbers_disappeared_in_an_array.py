from __future__ import annotations
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length, ans = len(nums), []
        nums = set(nums)
        for n in range(1, length+1):
            if n not in nums:
                ans.append(n)

        return ans


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)).difference(set(nums)))


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        ans = []
        for i, n in enumerate(nums):
            if n > 0:
                ans.append(i+1)

        return ans
