from __future__ import annotations


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 and\
            0b1010101010101010101010101010101 & n == n
