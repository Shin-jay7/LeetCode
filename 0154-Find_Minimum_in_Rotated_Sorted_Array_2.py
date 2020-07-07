from __future__ import annotations


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums: return None
        if n == 1 or nums[-1] > nums[0]: return nums[0]

        lo, hi = 0, n-1

        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1

        return nums[lo]
        # print(nums[lo])
        # return


test = Solution()
test.findMin([1,3,5]) # 1

test = Solution()
test.findMin([2,2,2,0,1]) # 0

test = Solution()
test.findMin([1,1]) # 1

test = Solution()
test.findMin([3,1,3,3]) # 1

test = Solution()
test.findMin([10,10,10,1,10]) # 1
