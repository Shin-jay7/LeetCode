from __future__ import annotations
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp_length[i] = length of longest increasing subsequence ending at i
        # dp_cnt[i] = number of longest increasing subsequences ending at i
        max_length, dp_length, dp_cnt = 0, [1]*n, [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp_length[j] == dp_length[i]:
                        dp_length[i] = dp_length[j] + 1
                        dp_cnt[i] = dp_cnt[j]
                    elif dp_length[j] + 1 == dp_length[i]:
                        dp_cnt[i] += dp_cnt[j]
            max_length = max(max_length, dp_length[i])
        return sum(
             num for idx, num in enumerate(dp_cnt)
             if dp_length[idx] == max_length
            )
