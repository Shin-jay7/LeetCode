from __future__ import annotations
from typing import List


# The meet point must be somewhere between current min and max. No matter which
# point you pick, the total running length for min and max is the same, 
# i.e. abs(min_point-meet_point)+abs(max_point-meet_point) = SOME_CONSTANT.
# So, we can effectively reduce the problem size from n to n-2 by discarding
# min and max points. Do you see it? That is the definition of median, isn't it?
# 
# Usually, minimized absolute differences => median; 
# minimized squared differences => mean
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))
        # tilde operation flips all bits 0 to 1 and 1 to 0
        # ~i = -i-1
