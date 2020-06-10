from __future__ import annotations


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)
        dp = self.check(s, wordDict, n)

        self.dfs(s, n, dp, 0, wordDict, '', ans)

        return ans

    def dfs(self, s, n, dp, idx, dic, path, ans):
        if dp[idx+n]:
            if not s:
                ans.append(path[:-1])
                return
            for i in range(1, n+1):
                if s[:i] in dic:
                    self.dfs(s[i:], len(s[i:]), dp, idx+i, dic, path+s[:i]+" ", ans)

    def check(self, s, dic, n):
        dp = [True] + [False] * n

        for i in range(1, n+1):
            for word in dic:
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]

        return dp


test = Solution()
test.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
"""
[
  "cats and dog",
  "cat sand dog"
]
"""

test = Solution()
test.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
"""
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
"""

test = Solution()
test.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
"""
[]
"""
