from __future__ import annotations


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                l_idx = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                r_idx = j
                break

        return [l_idx, r_idx]


test = Solution()
test.searchRange([5,7,7,8,8,10], 8) # [3,4]

test = Solution()
test.searchRange([5,7,7,8,8,10], 6) # [-1,-1]
