from __future__ import annotations
from typing import List
from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for key, value in Counter(nums).items():
            if value == 2:
                ans.append(key)

        return ans


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        # when you encounter k, change the value of index k
        # to negative as seen mark. If the value of index k 
        # is already negative, the value is duplicated.
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        
        return ans


test = Solution()
test.findDuplicates([4,3,2,7,8,2,3,1]) # [2,3]

test = Solution()
test.findDuplicates([1,1,2]) # [1]

test = Solution()
test.findDuplicates([1]) # []
