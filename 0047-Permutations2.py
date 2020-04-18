from __future__ import annotations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, [], ans)
        # print(ans)
        return ans

    def dfs(self, nums, perm, ans):
        if not nums and not perm in ans:
            ans.append(perm)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], perm+[nums[i]], ans)




test = Solution()
test.permuteUnique([1,1,2])
"""
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
