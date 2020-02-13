from __future__ import annotations

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #

test = Solution()
test.isMatch("aa", "a") # False

test = Solution()
test.isMatch("aa", "a*") # True

test = Solution()
test.isMatch("ab", ".*") # True

test = Solution()
test.isMatch("aab", "c*a*b") # True

test = Solution()
test.isMatch("mississippi", "mis*is*p*.") # False
