from __future__ import annotations


class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = 0

        for idx, letter in enumerate(s[::-1]):
            ans += 26**idx*(alphabet.index(letter)+1)

        return ans


test = Solution()
test.titleToNumber("A") # 1

test = Solution()
test.titleToNumber("AB") # 28

test = Solution()
test.titleToNumber("ZY") # 701
