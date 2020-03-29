from __future__ import annotations


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0

        while dividend >= divisor:
            i = 0
            while dividend >= divisor << (i+1):
                i += 1
            ans += 1 << i
            dividend -= divisor << i

        if not positive:
            ans *= -1

        return min(max(-(2**31), ans), (2**31)-1)


test = Solution()
test.divide(20, 3) # 6

test = Solution()
test.divide(7, -3) # -2

test = Solution()
test.divide(10, -3) # -3

test = Solution()
test.divide(-10, 3) # -3

test = Solution()
test.divide(-10, -3) # 3
