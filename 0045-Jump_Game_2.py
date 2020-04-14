from __future__ import annotations


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0

        n, start, end, step, max_ = len(nums), 0, nums[0], 1, 0
        while end < n-1:
            step += 1
            for i in range(start, end+1):
                if nums[i]+i >= n-1:
                    return step
                max_ = max(max_, nums[i]+i)
            start, end = end, max_

        return step


test = Solution()
test.jump([2,3,1,1,4]) # 2
