from __future__ import annotations


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1,len(nums),2):
            if not nums[i] == nums[i-1]:
                return nums[i-1]

        return nums[-1]


# 2*(a+b+c) - (a+a+b+b+c) = c
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) -sum(nums)


test = Solution()
test.singleNumber([2,2,1]) # 1

test = Solution()
test.singleNumber([4,1,2,1,2]) # 4
