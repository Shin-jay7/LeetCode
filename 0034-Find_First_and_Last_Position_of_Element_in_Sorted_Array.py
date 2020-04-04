from __future__ import annotations


class Solution:
    def insertion_idx(self, nums, target, left):
        l, r = 0, len(nums)

        while l < r:
            mid = (l+r)//2
            if nums[mid] > target or (left and target == nums[mid]):
                r = mid
            else:
                l = mid+1

        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l_idx = self.insertion_idx(nums, target, True)

        if l_idx == len(nums) or nums[l_idx] != target:
            return [-1, -1]

        return [l_idx, self.insertion_idx(nums, target, False)-1]


test = Solution()
test.searchRange([5,7,7,8,8,10], 8) # [3,4]

test = Solution()
test.searchRange([5,7,7,8,8,10], 6) # [-1,-1]
