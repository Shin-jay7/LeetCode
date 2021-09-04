from __future__ import annotations
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        # print(low, mid, high)

        while high > low:
            cnt = 0
            for n in nums:
                if mid < n <= high:
                    cnt += 1
            if cnt > high - mid: # then we have duplicates between mid-high
                low = mid + 1
            else:
                high = mid
            mid = (low + high) // 2
            # print(low, mid, high)

        return high


test = Solution()
test.findDuplicate( [1,3,4,2,2]) # 2
