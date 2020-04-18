from __future__ import annotations


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2

        return ans


test = Solution()
test.myPow(2.00000, 10) # 1024.00000

test = Solution()
test.myPow(2.10000, 3) # 9.26100

test = Solution()
test.myPow(2.00000, -2) # 0.25000

test = Solution()
test.myPow(2.00000, 0) # 2.00000
