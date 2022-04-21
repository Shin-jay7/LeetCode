from __future__ import annotations


# s has two or more repeated blocks. 
# After the first and last letter are deleted from s+s, 
# the remaining letters must include s. 
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False

        ss = (s + s)[1:-1]
        return s in ss
