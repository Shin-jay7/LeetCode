from __future__ import annotations


class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end, max_, step = 0, 0, 0, 0
        while end < len(nums)-1:
            step += 1
            for i in range(start, end+1):
                max_ = max(max_, nums[i]+i)
            start, end = end+1, max_

        return step


test = Solution()
test.jump([2,3,1,1,4]) # 2
