from __future__ import annotations
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            if num in nums2:
                ans.append(num)
                nums2.remove(num)

        return ans


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
