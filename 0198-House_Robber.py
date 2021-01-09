from __future__ import annotations

"""
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max(f(k-2) + nums[k], f(k-1))
"""

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         prev = curr = 0
#         for num in nums:
#             prev, curr = curr, max(prev + num, curr)

#         return curr
#         # print(curr)


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        memo = [-1] * (length+1)

        return self._rob(nums, length-1, memo)

    def _rob(self, nums, i, memo):
        if i < 0:
            return 0
        if memo[i] >= 0:
            return memo[i]
        result = max(_rob(nums, i-2, memo)+nums[i], _rob(nums, i-1, memo))
        memo[i] = result
        return result



test = Solution()
test.rob([1,2,3,1]) # 4

test = Solution()
test.rob([2,7,9,3,1]) # 12

test = Solution()
test.rob([2,1,1,2]) # 4