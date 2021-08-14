from __future__ import annotations


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        left, right = 1, 1

        for i in range(len(nums)):
            ans[i] *= left
            ans[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]

        return ans

# left *= nums[i] is the update after the multiply ans[i] *= left, 
# so that left will contain the product of all numbers that are left 
# to nums[i]
# similarly, right goes in the opposite direction, and right contains
# the product of numbers that are right to nums[i]
# so that nums[i] itself is not in the product.
