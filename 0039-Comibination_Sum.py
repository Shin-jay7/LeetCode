from __future__ import annotations


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        # print(ans)
        return ans

    def dfs(self, nums, remain, idx, comb, ans):
        # print(ans,comb,remain)
        if remain == 0:
            ans.append(comb)
            return
        for i in range(idx,len(nums)):
            if nums[i] > remain:
                break
            self.dfs(nums, remain-nums[i], i, comb+[nums[i]], ans)


test = Solution()
test.combinationSum([2,3,6,7], 7) # [[7],[2,2,3]]

test = Solution()
test.combinationSum([2,3,5],8) # [[2,2,2,2],[2,3,3],[3,5]]
