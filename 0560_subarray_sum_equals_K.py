from __future__ import annotations
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, cur, ans = {0: 1}, 0, 0

        for num in nums:
            cur += num
            ans += cnt.get(cur-k, 0)
            cnt[cur] = cnt.get(cur, 0) + 1

        return ans
