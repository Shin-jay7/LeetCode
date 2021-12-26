from __future__ import annotations
from typing import List
import pandas as pd


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        dp, dpPrev, ans = 0, 0, 0
        for i in range(2, length):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp = dpPrev + 1
            ans += dp
            dpPrev, dp = dp, 0

        return ans


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # := は式の途中結果を紐づけることができる
        return sum((k := sum(1 for _ in g))*(k-1)//2 for _,g in pd.groupby(nums[i+1]-nums[i] for i in range(len(nums)-1)))


test = Solution()
test.numberOfArithmeticSlices([1,2,3,4]) # 3

test = Solution()
test.numberOfArithmeticSlices([1,2,3,8,9,10]) # 2
