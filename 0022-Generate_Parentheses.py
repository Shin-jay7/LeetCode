from __future__ import annotations


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def searchPattern(pattern = '', left = 0, right = 0):
            if len(pattern) == 2 * n:
                ans.append(pattern)
                return
            if left < n:
                searchPattern(pattern+'(', left+1, right)
            if right < left:
                searchPattern(pattern+')', left, right+1)

        searchPattern()
        return ans


test = Solution()
test.generateParenthesis(3)
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
