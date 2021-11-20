from __future__ import annotations
from string import ascii_lowercase


class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx = list(
            s.index(char) for char in ascii_lowercase
            if s.count(char) == 1
            )
        return min(idx) if len(idx) > 0 else -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d, seen = {}, set()
        for idx, char in enumerate(s):
            if char not in seen:
                d[char] = idx
                seen.add(char)
            elif char in d:
                del d[char]
        return next(iter(d.values())) if d else -1
