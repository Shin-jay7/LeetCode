from __future__ import annotations


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for idx in range(len(s)):
            if not s[idx] == t[idx]:
                return t[idx]

        return t[-1]
