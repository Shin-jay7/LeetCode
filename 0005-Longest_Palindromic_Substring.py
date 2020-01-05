from __future__ import annotations


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(longest) >= j-i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    longest = s[i:j]
                    break

        return longest
        # print(longest)


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

