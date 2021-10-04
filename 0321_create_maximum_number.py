from __future__ import annotations
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int)\
            -> List[int]:
        def pre_round(nums, idx):
            cnt = len(nums) - idx
            candidates = []
            for num in nums:
                while cnt and candidates and candidates[-1] < num:
                    candidates.pop()
                    cnt -= 1
                candidates.append(num)
            return candidates[:idx]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]

        return max(merge(pre_round(nums1, i), pre_round(nums2, k-i))
                   for i in range(k+1)
                   if i <= len(nums1) and k-i <= len(nums2))
        # print(max(merge(pre_round(nums1, i), pre_round(nums2, k-i))
        #           for i in range(k+1)
        #           if i <= len(nums1) and k-i <= len(nums2)))


test = Solution()
test.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) # [9,8,6,5,3]

test = Solution()
test.maxNumber([6,7], [6,0,4], 5) # [6,7,6,0,4]

test = Solution()
test.maxNumber([3,9], [8,9], 3) # [9,8,9]
