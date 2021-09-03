from __future__ import annotations
import bisect


class Solution:
    def firstBadVersion(self, n):
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, lo=0, hi=n)
