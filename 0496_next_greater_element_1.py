from __future__ import annotations
from typing import List


class Solution:
    def nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
       ) -> List[int]:
        nges, stack = {}, []
        for num in nums2:
            while stack and stack[-1] < num:
                prev = stack.pop()
                nges[prev] = num
            stack.append(num)

        return [nges.get(num, -1) for num in nums1]


test = Solution()
test.nextGreaterElement([4,1,2], [1,3,4,2])
