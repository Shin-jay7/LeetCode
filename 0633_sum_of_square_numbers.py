from __future__ import annotations
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i > j:
            _sum = i**2 + j**2
            if _sum == c:
                return True
            elif _sum < c:
                i += 1
            else:
                j -= 1
        return False
