from __future__ import annotations
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd, even = False, 0
        for val in Counter(s).values():
            if val % 2:
                odd = True
            even += (val // 2) * 2

        return even + 1 if odd else even
