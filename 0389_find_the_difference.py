from __future__ import annotations


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        unicode = 0
        for ch in s+t:
            unicode ^= ord(ch)
        return chr(unicode)
