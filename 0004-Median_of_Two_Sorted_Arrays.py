from __future__ import annotations
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(sorted(nums1+nums2))


test = Solution()
nums1 = [1, 3]
nums2 = [2]
test.findMedianSortedArrays(nums1, nums2) # 2.0

test = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
test.findMedianSortedArrays(nums1, nums2) # 2.5
