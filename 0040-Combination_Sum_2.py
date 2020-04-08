from __future__ import annotations


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.dfs(candidates, 0, target, [], ans)
        # print(ans)
        return ans

    def dfs(self, nums, start, remain, comb, ans):
        if remain == 0:
            ans.append(comb)
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            if nums[i] > remain:
                break
            self.dfs(nums, i+1, remain-nums[i], comb+[nums[i]], ans)


test = Solution()
test.combinationSum2([1,2], 4) # [[]]

test = Solution()
test.combinationSum2([10,1,2,7,6,1,5], 8) # [[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]

test = Solution()
test.combinationSum2([2,5,2,1,2], 5) # [[1,2,2],[5]]
