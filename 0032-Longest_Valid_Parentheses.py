from __future__ import annotations


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    max_ = max(max_, i-stack[-1])

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

test = Solution()
test.longestValidParentheses("(()))())(") # 4

test = Solution()
test.longestValidParentheses("()(())") # 6
