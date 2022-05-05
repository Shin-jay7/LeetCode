from __future__ import annotations
import math


# n = k^m + k^(m-1) + ... + k + 1
# n > k^m
# mth root of n > k
# 
# n = k^m + ... + 1 < (k+1)^m ...
# 
# K+1 > mth root of n > k
# 
# k is a base and m = number of 1s - 1
# 
# m must be between 2 and log2n. Otherwise n - 1
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(math.log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n**m**-1)
            if (k**(m + 1) - 1) // (k - 1) == n:
                return str(k)

        return str(n - 1)
        # when m = 1, k is n-1 because (n-1)^1 + (n-1)^0 = n
