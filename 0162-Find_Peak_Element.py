from __future__ import annotations


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0 or n == 1: return 0

        if n == 2:
            if nums[1] > nums[0]:
                return 1
            else:
                return 0

        if n > 2:
            if nums[0] > nums[1]:
                return 0

        if nums[-1] > nums[-2]:
            return n-1

        for i in range(1,n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
                # print(i)
                # return


test = Solution()
test.findPeakElement([1,2,3,1]) # 2

test = Solution()
test.findPeakElement([1,2,1,3,5,6,4]) # 1

test = Solution()
test.findPeakElement([1]) # 0

test = Solution()
test.findPeakElement([]) # 0

test = Solution()
test.findPeakElement([1,2]) # 1

test = Solution()
test.findPeakElement([2,1]) # 0

test = Solution()
test.findPeakElement([2,2]) # 0

test = Solution()
test.findPeakElement([3,2,1]) # 0

test = Solution()
test.findPeakElement([1,2,3]) # 2
