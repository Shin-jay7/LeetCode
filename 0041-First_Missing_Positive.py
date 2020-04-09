from __future__ import annotations


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        while True:
            if i not in nums:
                # print(i)
                # return
                return i
            else:
                i += 1


test = Solution()
test.firstMissingPositive([1,2,0]) # 3

test = Solution()
test.firstMissingPositive([3,4,-1,1]) # 2

test = Solution()
test.firstMissingPositive([7,8,9,11,12]) # 1
