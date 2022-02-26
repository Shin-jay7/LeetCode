from __future__ import annotations
from typing import List


# https://leetcode.com/problems/non-overlapping-intervals/discuss/276056/Python-Greedy-Interval-Scheduling
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        boader, ans = float('-inf'), 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start >= boader:
                boader = end
            else:
                ans += 1

        return ans
