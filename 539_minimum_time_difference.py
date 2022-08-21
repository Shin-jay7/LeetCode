from __future__ import annotations
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted(int(t[:2]) * 60 + int(t[-2:]) for t in timePoints)
        times.append(times[0] + 1440)
        return min(b-a for a, b in zip(times, times[1:]))
