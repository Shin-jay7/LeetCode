from __future__ import annotations
import bisect


class Solution:
    def guessNumber(self, n: int) -> int:
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect.bisect(C(), -1, 1, n)


class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid

        return lo
