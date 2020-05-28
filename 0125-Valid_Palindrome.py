from __future__ import annotations
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W', "", s)
        s = s.upper()

        return s == s[::-1]
        # print(s == s[::-1])


test = Solution()
test.isPalindrome("A man, a plan, a canal: Panama") # True

test = Solution()
test.isPalindrome("race a car") # False

test = Solution()
test.isPalindrome("rac a car") # True
