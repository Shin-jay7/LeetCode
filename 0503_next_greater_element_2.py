from __future__ import annotations
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack, ans = [], [-1] * length
        for i in list(range(length)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                ans[stack.pop()] = nums[i]
            stack.append(i)

        return ans
