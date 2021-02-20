from __future__ import annotations


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        for i in range(len(s)+1): # +1 is required for s == ""
            if s.startswith(rev[i:]):
                return rev[:i] + s


test = Solution()
test.shortestPalindrome("")
