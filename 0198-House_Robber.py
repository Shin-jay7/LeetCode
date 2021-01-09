from __future__ import annotations

"""
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max(f(k-2) + nums[k], f(k-1))
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)

        return curr
        # print(curr)


test = Solution()
test.rob([1,2,3,1]) # 4

test = Solution()
test.rob([2,7,9,3,1]) # 12

test = Solution()
test.rob([2,1,1,2]) # 4