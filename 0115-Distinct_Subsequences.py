from __future__ import annotations


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] * (len(s)+1)

        for t_char in t:
            prev, dp[0] = dp[0], 0
            for i, s_char in enumerate(s,1):
                curr = dp[i]
                dp[i] = dp[i-1] + (t_char == s_char and prev)
                prev = curr

        return dp[-1]
        # print(dp[-1])


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        matches = [1] + [0]*len(t)

        for i in range(len(s)):
            for j in reversed(range(len(t))):
                if t[j] == s[i]:
                    matches[j+1] += matches[j]

        return matches[-1]
        # print(matches[-1])


test = Solution()
test.numDistinct("rabbbit", "rabbit") # 3

test = Solution()
test.numDistinct("babgbag", "bag") # 5
