from __future__ import annotations


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


test = Solution()
test.majorityElement([3,2,3]) # 3

test = Solution()
test.majorityElement([2,2,1,1,1,2,2]) # 2
