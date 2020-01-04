from __future__ import annotations


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = sorted(nums1+nums2)
        mid, odd = len(L)//2, len(L)%2
        return float(L[mid]) if odd else (L[mid-1]+L[mid])/2


test = Solution()
nums1 = [1, 3]
nums2 = [2]
test.findMedianSortedArrays(nums1, nums2) # 2.0

test = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
test.findMedianSortedArrays(nums1, nums2) # 2.5
