from __future__ import annotations


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Do not allocate extra space for another array, you must do this
        by modifying the input array in-place with O(1) extra memory.
        """
        i = 0

        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1

        return i


test = Solution()
test.removeDuplicates([1,1,1,2,2,3]) # 5

test = Solution()
test.removeDuplicates([0,0,1,1,1,1,2,3,3]) # 7
