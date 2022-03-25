from __future__ import annotations
from typing import List


# Brute force & Time limit exceeded solution
# 
# Increase min_num until it catches up with max_num
# Then new_min_num is incremented original min_num,
# find new_max_num, and continue the same until you have all equal nums.
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        while True:
            max_num, min_num = max(nums), min(nums)
            if max_num == min_num:
                break
            diff = max_num - min_num
            ans += diff
            idx = nums.index(max_num)
            for i in range(len(nums)):
                nums[i] = nums[i] + diff if i != idx else nums[i]

        return ans


# Math solution
# 
# sum(nums) + ans * (len(nums)-1) = final_num * len(nums)
# Pleas notice minimum_num is always minimum until it reaches final_num.
# final_num = minimum_num + ans
# sum(nums) + ans * (len(nums)-1) = (minimum_num + ans) * len(nums)
# sum(nums) + ans * (len(nums)-1) = minimum_num * len(nums) + ans * len(nums)
# ans = sum(nums) - minimu_num * len(nums)
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
