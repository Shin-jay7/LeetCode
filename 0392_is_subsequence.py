from __future__ import annotations


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # turned t into a iterator, and what that does is that 
        # "c in iterator" iterates through the iterator until 
        # the first position where it finds a match.
        iterator = iter(t)
        return all(ch in iterator for ch in s)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        pos = 0
        for ch in t:
            if ch == s[pos]:
                pos += 1
                if pos == len(s):
                    return True
        return False
        