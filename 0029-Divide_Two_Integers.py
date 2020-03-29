from __future__ import annotations


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1

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
