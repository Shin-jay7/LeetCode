from __future__ import annotations


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        for i in range(length-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = i
                while j < length and nums[j] > nums[i-1]:
                    idx = j
                    j += 1
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
                nums[i:] = sorted(nums[i:])
                return

        nums.reverse()


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
