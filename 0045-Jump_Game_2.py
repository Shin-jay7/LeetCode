from __future__ import annotations


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0

        start, end, step, max_ = 0, nums[0], 1, 0
        while end < len(nums)-1:
            step += 1
            for i in range(start, end+1):
                max_ = max(max_, nums[i]+i)
            start, end = end, max_

        return step


test = Solution()
test.jump([2,3,1,1,4]) # 2
