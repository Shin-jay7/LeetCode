from __future__ import annotations
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        for num in nums1:
            if num in nums2:
                ans.add(num)

        return list(ans)
        # print(list(ans))


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


test = Solution()
test.intersection([1,2,2,1], [2,2]) # [2]

test = Solution()
test.intersection([4,9,5], [9,4,9,8,4]) # [4, 9]
