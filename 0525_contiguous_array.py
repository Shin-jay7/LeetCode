from __future__ import annotations
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, max_len = 0, 0
        # Without this intializer, you are not going to have right results for
        # nums array which have results from the beginning, such as [0,0,1,1]
        seen = {0: -1} 
        for idx, num in enumerate(nums):
            if num == 0:
                cnt -= 1
            else:
                cnt += 1
            if cnt in seen:
                max_len = max(max_len, idx-seen[cnt])
            else:
                seen[cnt] = idx

        return max_len
