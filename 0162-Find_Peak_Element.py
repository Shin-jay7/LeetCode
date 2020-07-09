from __future__ import annotations


# https://leetcode.com/problems/find-peak-element/solution/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1: return 0

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return i

        return n-1


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1: return 0
        if n == 2:
            return 0 if nums[0] > nums[1] else 1

        lo, hi = 0, n-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid-1] > nums[mid]:
                hi = mid-1
            elif nums[mid+1] > nums[mid]:
                lo = mid+1
            else:
                return mid

        return lo
        # print(lo)
        # return


test = Solution()
test.findPeakElement([1,2,3,4,5]) # 4

# test = Solution()
# test.findPeakElement([1,2,3,1]) # 2

# test = Solution()
# test.findPeakElement([1,2,1,3,5,6,4]) # 1

# test = Solution()
# test.findPeakElement([1]) # 0

# test = Solution()
# test.findPeakElement([]) # 0

# test = Solution()
# test.findPeakElement([1,2]) # 1

# test = Solution()
# test.findPeakElement([2,1]) # 0

# test = Solution()
# test.findPeakElement([2,2]) # 0

# test = Solution()
# test.findPeakElement([3,2,1]) # 0

# test = Solution()
# test.findPeakElement([1,2,3]) # 2

# test = Solution()
# test.findPeakElement([1,3,2,1]) # 2
