from __future__ import annotations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        self.dfs(nums, [], ans)
        # print(ans)
        return ans

    def dfs(self, nums, perm, ans):
        if not nums:
            ans.append(perm)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], perm+[nums[i]], ans)


test = Solution()
test.permute([1,2,3])
"""
  [
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
