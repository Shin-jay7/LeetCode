from __future__ import annotations


class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digits in range(1, 11):
            first = 10**(digits - 1) # first element of each digit group
            if n < 9 * first * digits:
                return int(str(first + n/digits)[n % digits])
            n -= 9 * first * digits