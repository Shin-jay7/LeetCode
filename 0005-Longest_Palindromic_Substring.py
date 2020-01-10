from __future__ import annotations
# import timeit


# code = """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""

        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        max_ = 1
        for i in range(n, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if max_ < j-i+1:
                            max_ = j-i+1
                            ans = s[i:j+1]

        return ans


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

test = Solution()
test.longestPalindrome("aaaa") # "aaaa"
# """

# print(timeit.timeit(code, number=10000))
