from __future__ import annotations


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ = 0

        def isValid(substr: str) -> bool:
            stack = []
            for i in range(len(substr)):
                if substr[i] == "(":
                    stack.append(substr[i])
                elif stack != []:
                    stack.pop()
                else:
                    return False
            return stack == []

        for i in range(len(s)):
            for j in range(i+2,len(s)+1,2):
                if isValid(s[i:j]):
                    max_ = max(max_, j-i)

        return max_
        # print(max_)


test = Solution()
test.longestValidParentheses("(()") # 2

test = Solution()
test.longestValidParentheses(")()())") # 4

test = Solution()
test.longestValidParentheses("()()") # 4

test = Solution()
test.longestValidParentheses("()(()") # 2
