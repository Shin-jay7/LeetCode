from __future__ import annotations


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
                # print(i)
                # return

        return len(nums)
        # print(len(nums))


test = Solution()
test.searchInsert([1,3,5,6], 5) # 2

test = Solution()
test.searchInsert([1,3,5,6], 2) # 1

test = Solution()
test.searchInsert([1,3,5,6], 7) # 4

test = Solution()
test.searchInsert([1,3,5,6], 0) # 0
