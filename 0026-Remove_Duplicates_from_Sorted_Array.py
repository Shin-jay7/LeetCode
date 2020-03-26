from __future__ import annotations


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []: return 0

        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i+1


test = Solution()
test.removeDuplicates([1,1,2]) # 2
