from __future__ import annotations


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(self, s: str) -> bool:
            return s == s[::-1]
        i, j = 0, len(s)-1
        while i < j:
            if not s[i] == s[j]:
                delete_i = s[:i] + s[i+1:]
                delete_j = s[:j] + s[j+1:]
                return isPalindrome(self, delete_i)\
                    or isPalindrome(self, delete_j)
            i += 1
            j -= 1
        return True


test = Solution()
test.validPalindrome("abca") # True
