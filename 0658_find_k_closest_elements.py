from __future__ import annotations
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        size = len(arr)
        left, right = 0, size-1
        for _ in range(size-k):
            if arr[right]-x >= x-arr[left]:
                right -= 1
            else:
                left += 1
        return arr[left:right+1]


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k
        while left < right:
            mid = (left+right) // 2
            if arr[mid+k]-x >= x-arr[mid]:
                right = mid
            else:
                left = mid+1
        return arr[left:left+k]


test = Solution()
test.findClosestElements([1,2,3,4,5], 4, 3)  # [1,2,3,4]

test = Solution()
test.findClosestElements([1,2,3,4,5], 4, -1)  # [1,2,3,4]

test = Solution()
test.findClosestElements([1], 1, 1)  # [1]

test = Solution()
test.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)  # [3,6,8,8,9]
