from __future__ import annotations


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums: return None
        if n == 1: return nums[0]
        if nums[-1] > nums[0]: return nums[0]

        lo, hi = 0, n-1

        while lo <= hi:
            mid = (lo+hi+1)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
                # print(nums[mid])
                # return
            elif nums[mid] > nums[0]:
                lo = mid+1
            else:
                hi = mid-1


test = Solution()
test.findMin([1]) # 1

test = Solution()
test.findMin([2,1]) # 1

test = Solution()
test.findMin([3,4,5,1,2]) # 1

test = Solution()
test.findMin([4,5,6,7,0,1,2]) # 0
