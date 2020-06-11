from __future__ import annotations


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)

        dp = [True] + [False] * n
        for i in range(1, n+1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]

        self.dfs(s, n, dp, 0, wordDict, '', ans)

        return ans

    def dfs(self, s, n, dp, idx, dic, path, ans):
        if dp[idx+n]:
            if not s:
                ans.append(path[:-1])
                return
            for i in range(1, n+1):
                if s[:i] in dic:
                    self.dfs(s[i:], len(s[i:]), dp, idx+i,\
                             dic, path+s[:i]+" ", ans)


from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache()

        def dp(i):
            ans = []
            for word in wordDict:
                if word != s[i:i+len(word)]:
                    continue
                elif len(word) == len(s)-i:
                    ans.append(word)
                else:
                    for rest in dp(i+len(word)):
                        ans.append(word + ' ' + rest)

            return ans

        return dp(0)
        # print(dp(0))

# Concise but slow
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s [i:j] in wordDict
                           for tail in sentences(j)]

            return memo[i]

        return sentences(0)
        # print(sentences(0))



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
