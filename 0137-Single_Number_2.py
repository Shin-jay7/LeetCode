from __future__ import annotations


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(2,len(nums),3):
            if not (nums[i] == nums[i-1] and nums[i] == nums[i-2]):
                return nums[i-2]

        return nums[-1]


test = Solution()
test.singleNumber([2,2,3,2]) # 3

test = Solution()
test.singleNumber([0,1,0,1,0,1,99]) # 99
