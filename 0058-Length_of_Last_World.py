from __future__ import annotations


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s.replace(" ", ""):
            return 0

        # print(len(s.split()[-1]))
        return len(s.split()[-1])


test = Solution()
test.lengthOfLastWord("Hello World") # 5

test = Solution()
test.lengthOfLastWord("") # 0

test = Solution()
test.lengthOfLastWord("      ") # 0
