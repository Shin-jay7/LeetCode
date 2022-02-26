from __future__ import annotations
from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> int:
        ans = []
        lst = sorted(
            (interval[0], idx) for idx, interval in enumerate(intervals))

        for interval in intervals:
            pos = bisect_left(lst, (interval[1],))
            ans.append(lst[pos][1] if pos != len(intervals) else -1)

        return ans
