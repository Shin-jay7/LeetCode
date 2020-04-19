from __future__ import annotations


# Kadane's algorithm
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1]+nums[i])

        return max(nums)


test = Solution()
test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) # 6
