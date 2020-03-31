from __future__ import annotations


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return

        k = i-1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]

        nums[i:] = sorted(nums[i:])


test = Solution()
test.nextPermutation([1,3,2]) # [2,1,3]

test = Solution()
test.nextPermutation([1,2,3]) # [1,3,2]

test = Solution()
test.nextPermutation([3,2,1]) # [1,2,3]

test = Solution()
test.nextPermutation([1,1,5]) # [1,5,1]

test = Solution()
test.nextPermutation([1,5,1]) # [5,1,1]
