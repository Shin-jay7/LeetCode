from __future__ import annotations
from typing import List


# If sum(nums[i:j]) % == 0 when i < j,
# then sum(nums[:j]) % k == sum(nums[:i]) % k
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder, seen = 0, {0: -1}
        for idx, num in enumerate(nums):
            remainder = (remainder + num) % k
            if remainder not in seen:
                seen[remainder] = idx
            elif idx - seen[remainder] > 1:
                return True
        return False
