from __future__ import annotations


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ = 0
        l, r = 0, 0

        for i in range(len(s)):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_ = max(max_, l+r)
            elif r >= l:
                l, r = 0, 0

        l, r = 0, 0

        for j in range(len(s)-1,-1,-1):
            if s[j] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_ = max(max_, l+r)
            elif l >= r:
                l, r = 0, 0

        return max_
        print(max_)


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
