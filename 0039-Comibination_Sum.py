from __future__ import annotations


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        # print(ans)
        return ans

    def dfs(self, nums, target, idx, sum_, ans):
        if target == 0:
            ans.append(sum_)
            return
        for i in range(idx,len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i, sum_+[nums[i]], ans)


test = Solution()
test.combinationSum([2,3,6,7], 7) # [[7],[2,2,3]]

test = Solution()
test.combinationSum([2,3,5],8) # [[2,2,2,2],[2,3,3],[3,5]]
