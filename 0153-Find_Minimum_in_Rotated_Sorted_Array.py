from __future__ import annotations


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums: return None
        if n == 1: return nums[0]

        i = 0
        while i < n-1:
            if nums[i-1] > nums[i] and nums[i+1] > nums[i]:
                return nums[i]
                # print(nums[i])
                # return
            i += 1

        return nums[-1]
        # print(nums[-1])
        # return


test = Solution()
test.findMin([1] ) # 1

test = Solution()
test.findMin([2,1] ) # 1

test = Solution()
test.findMin([3,4,5,1,2] ) # 1

test = Solution()
test.findMin([4,5,6,7,0,1,2]) # 0
