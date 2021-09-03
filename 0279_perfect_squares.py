from __future__ import annotations
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        if int(sqrt(n))**2 == n:
            return 1

        for i in range(int(sqrt(n)) + 1):
            if int(sqrt(n - i*i))**2 == n - i*i:
                return 2

        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4

        return 3

# https://leetcode.com/problems/perfect-squares/discuss/707526/Python-Fastest-O(sqrt(n))-solution-with-math-explanied.
