from __future__ import annotations
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455658/C%2B%2BJavaPython-DP-with-Picture-explained-Clean-and-Concise
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]
                dp[i][diff] += cnt + 1
                ans += cnt

        return ans
