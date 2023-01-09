from __future__ import annotations
import math


# a^2 + b^2 = c
# a = sqrt(c - b^2)
# a <= sqrt(c)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b = math.sqrt(c - a**2)
            if b == int(b):
                return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_set = set()
        for x in range(int(math.sqrt(c))+1):
            square_set.add(x**2)
        for a_square in square_set:
            b_square = c - a_square
            if b_square in square_set:
                return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i <= j:
            _sum = i**2 + j**2
            if _sum == c:
                return True
            elif _sum < c:
                i += 1
            else:
                j -= 1
        return False
