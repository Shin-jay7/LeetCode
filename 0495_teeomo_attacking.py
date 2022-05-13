from __future__ import annotations
from typing import List


class Solution:
    def findPoisonedDuration(slef, timeSeries: List[int], duration: int) -> int:
        _sum, end = 0, 0
        for t in timeSeries:
            if t >= end:
                _sum += duration
            else:
                _sum += (duration - (end - t))
            end = t + duration

        return _sum
