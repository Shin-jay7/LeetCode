from __future__ import annotations
from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            idx = bisect_left(ans, num)
            if idx == len(ans):
                ans.append(num)
            else:
                ans[idx] = num
        
        return len(ans)


test = Solution()
test.lengthOfLIS( [10,9,2,5,3,7,101,18]) # 4
