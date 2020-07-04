from __future__ import annotations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        revNums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1 # 1 required in case nums[i-1] == 0
            revNums[i] *= revNums[i-1] or 1

        return max(nums+revNums)


test = Solution()
test.maxProduct([-2,3,-4]) # 24

test = Solution()
test.maxProduct([0,2]) # 2

test = Solution()
test.maxProduct([-3,-1,-1]) # 3

test = Solution()
test.maxProduct([2,3,-2,4]) # 6

test = Solution()
test.maxProduct([-2,0,-1]) # 0

test = Solution()
test.maxProduct([1]) # 1

test = Solution()
test.maxProduct([]) # 0
