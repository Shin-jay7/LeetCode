from __future__ import annotations
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        accum = [0]
        for num in nums:
            accum.append(accum[-1] + num)

        def sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            cnt = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in accum[lo:mid]:
                while i < hi and accum[i] - left < lower:
                    i += 1
                while j < hi and accum[j] - left <= upper:
                    j += 1
                cnt += j - i
            accum[lo:hi] = sorted(accum[lo:hi])
            return cnt

        return sort(0, len(accum))
