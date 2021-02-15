from __future__ import annotations


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        i, ans = 0, length + 1
        for j in range(length):
            target -= nums[j]
            while target <= 0:
                ans = min(ans, j - i + 1)
                target += nums[i]
                i += 1
        return ans % (length + 1)
