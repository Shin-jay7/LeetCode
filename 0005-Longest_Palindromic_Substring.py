from __future__ import annotations


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i in range(len(s)):
            length1 = expandAroundCenter(s, i, i)
            length2 = expandAroundCenter(s, i, i+1)
            length = max(length1, length2)
            if length > end-start:
                start = i - (length-1)//2
                end = i + length//2

        # return s[start:end+1]
        print(s[start:end+1])

def expandAroundCenter(s: str, L: int, R: int) -> int:
    while L >=0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1

    return R - L - 1


test = Solution()
test.longestPalindrome("") # ""

test = Solution()
test.longestPalindrome(" ") # ""

test = Solution()
test.longestPalindrome("a") # "a"

test = Solution()
test.longestPalindrome("bb") # "bb"

test = Solution()
test.longestPalindrome("babad") # "bab" or "aba"

test = Solution()
test.longestPalindrome("cbbd") # "bb"

