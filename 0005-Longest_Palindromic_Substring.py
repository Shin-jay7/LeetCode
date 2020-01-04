from __future__ import annotations


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_, i, j = "", 0, 0

        for i in range(n):
            while i < n and j < n:
                word = s[i:j+1]
                if word == word[::-1] and len(word) > len(max_):
                    max_ = word
                    i = j+1
                    j = i
                j += 1

        # return max_
        print(max_)


test = Solution()
test.longestPalindrome("") # ""

test = Solution()
test.longestPalindrome(" ") # ""

test = Solution()
test.longestPalindrome("a") # "a"

test = Solution()
test.longestPalindrome("babad") # "bab" or "aba"

test = Solution()
test.longestPalindrome("cbbd") # "bb"

