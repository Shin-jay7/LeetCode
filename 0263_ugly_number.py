from __future__ import annotations


class Solution:
    def isUgly(self, n: int) -> bool:
        for p in [10, 8, 6, 5, 4, 3, 2]:
            while n % p == 0:
                n //= p

        return n == 1
        # print(n == 1)


test = Solution()
test.isUgly(6) # True
