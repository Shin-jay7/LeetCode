from __future__ import annotations
from functools import cache
from math import pow


# https://leetcode.com/problems/integer-break/discuss/285876/Python-O(1)-one-line-solution-detailed-explanation
class Solution:
    def integerBreak(self, n: int) -> int:
        return int(pow(2, (-n) % 3) * pow(3, (n-1) % 3 + (n-4)//3)) if n > 3 else n-1


# https://leetcode.com/problems/integer-break/discuss/383679/Python-DP-solution-with-detailed-explanation.-Avoids-confusion-about-factors-of-2-or-3.
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        for m in range(2, n+1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)

        return dp[n]
