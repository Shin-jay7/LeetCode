from __future__ import annotations


class Solution:
    def partition(self, s: str) -> List[List[int]]:
        ans = []
        self.dfs(s, [], ans)

        # print(ans)
        return ans

    def dfs(self, s, path, ans):
        if not s:
            ans.append(path)
            return

        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], ans)

    def isPalindrome(self, s):
        return s == s[::-1]


class Solution:
    def partition(self, s: str) -> List[List[int]]:
        return [[s[:i]] + rest
                for i in range(1,len(s)+1)
                if s[:i] == s[i-1::-1]
                for rest in self.partition(s[i:])] or [[]]


test = Solution()
test.partition("aab")
"""
[
  ["aa","b"],
  ["a","a","b"]
]
"""
