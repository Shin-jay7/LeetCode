from __future__ import annotations
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            cnt = 0
            while nums[i] != -1:
                nums[i], cnt, i = -1, cnt+1, nums[i]
            ans = max(ans, cnt)

        return ans
