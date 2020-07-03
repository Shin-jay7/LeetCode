from __future__ import annotations


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


test = Solution()
test.reverseWords("the sky is blue") # "blue is sky the"

test = Solution()
test.reverseWords("  hello world!  ") # "world! hello"

test = Solution()
test.reverseWords("a good   example") # "example good a"
