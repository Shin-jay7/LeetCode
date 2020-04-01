from __future__ import annotations


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_ = 0
        dp = [0]*len(s)

        for i in range(1,len(s)):
            if s[i] == ")" and s[i-1] == "(":
                dp[i] = dp[i-2] + 2
            elif s[i] == ")" and s[i-1] == ")":
                idx = i-dp[i-1]-1
                if idx >= 0 and s[idx] == "(":
                    idx = max(0, idx-1)
                    dp[i] = dp[idx] + dp[i-1] +  2
            max_ = max(max_, dp[i])

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
