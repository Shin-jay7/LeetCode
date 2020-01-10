from __future__ import annotations


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or s == " ":
            return ""

        n = len(s)

        L = [[[0, ""] for x in range(n)] for x in range(n)]

        for i in range(n):
            L[i][i][0] = 1
            L[i][i][1] = s[i]

        for cl in range(2, n+1):
            for i in range(n-cl+1):
                j = i+cl-1
                if s[i] == s[j] and cl == 2:
                    L[i][j][0] = 2
                    L[i][j][1] = s[i:j+1]
                elif s[i] == s[j] and L[i+1][j-1][0] == cl-2:
                    L[i][j][0] = cl
                    L[i][j][1] = s[i:j+1]
                else:
                    if L[i][j-1][0] > L[i+1][j][0]:
                        L[i][j] = L[i][j-1]
                    else:
                        L[i][j] = L[i+1][j]

        return L[0][n-1][1]


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

test = Solution()
test.longestPalindrome("abcda") # "a"

