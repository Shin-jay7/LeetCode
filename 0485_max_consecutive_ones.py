from __future__ import annotations
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, _max = 0, 0
        for n in nums:
            if n == 1:
                cnt += 1
            else:
                _max = max(_max, cnt)
                cnt = 0
            _max = max(_max, cnt)

        return _max
