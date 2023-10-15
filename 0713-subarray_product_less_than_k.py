from __future__ import annotations
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, ans, product = 0, 0, 1

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            ans += right - left + 1

        # print(ans)
        return ans


test = Solution()
test.numSubarrayProductLessThanK([10, 5, 2, 6], 100) # 8
