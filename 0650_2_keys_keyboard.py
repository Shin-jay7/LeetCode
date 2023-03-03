from __future__ import annotations
import math


class Solution:
    def minSteps(self, n: int) -> int:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.minSteps(n//i) + i
        return 0 if n == 1 else n
