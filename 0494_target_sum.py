from __future__ import annotations
from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        _sum = defaultdict(int)
        _sum[0] = 1
        for x in nums:
            tmp = defaultdict(int)
            for y in _sum:
                tmp[y + x] += _sum[y]
                tmp[y - x] += _sum[y]
            _sum = tmp

        return _sum[target]
