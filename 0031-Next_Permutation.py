from __future__ import annotations


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            # print(nums)
            return

        k = i-1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]

        l, r = k+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # print(nums)


test = Solution()
test.nextPermutation([1,2,3]) # [1,3,2]

test = Solution()
test.nextPermutation([3,2,1]) # [1,2,3]

test = Solution()
test.nextPermutation([1,1,5]) # [1,5,1]
