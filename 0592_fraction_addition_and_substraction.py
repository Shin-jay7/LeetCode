from __future__ import annotations
from fractions import Fraction
import re
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        ans = sum(map(Fraction,
                      expression.replace('+', ' +').replace('-', ' -').split())
                  )
        return '{0}/{1}'.format(ans.numerator, ans.denominator)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        ans = sum(map(Fraction, re.findall('[+-]?\d+/\d+', expression)))
        return '{0}/{1}'.format(ans.numerator, ans.denominator)


class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = map(int, re.findall('[+-]?\d+', expression))
        numerator, denominator = 0, 1
        for num in nums:
            num_next = next(nums)
            numerator = numerator * num_next + denominator * num
            denominator *= num_next
            g = math.gcd(numerator, denominator)
            numerator //= g
            denominator //=g
        return '{0}/{1}'.format(numerator, denominator)


test = Solution()
test.fractionAddition("1/3-1/2")
