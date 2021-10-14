from __future__ import annotations
from functools import cache
from math import pow

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(n, k):
            if n == 0:
                if k == 2:
                    return 1
                return 0
                
            ans = 0
            for x in range(1, n+1):
                ans = max(ans, dp(n-x, min(k+1, 2)) * x)
            return ans

        return dp(n, 0)


# https://leetcode.com/problems/integer-break/discuss/285876/Python-O(1)-one-line-solution-detailed-explanation
class Solution:
    def integerBreak(self, n: int) -> int:
        return int(pow(2, (-n) % 3) * pow(3, (n-1) % 3 + (n-4)//3)) if n > 3 else n-1
