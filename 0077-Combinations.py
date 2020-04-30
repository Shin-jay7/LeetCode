from __future__ import annotations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.dfs(n, k, ans, [], 1)

        return ans
        # print(ans)

    def dfs(self, n, k, ans, path, idx):
        if len(path) == k:
            ans.append(path)
            return

        for i in range(idx,n+1):
            self.dfs(n, k, ans, path+[i], i+1)


test = Solution
test.combine(4, 2)
"""
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
