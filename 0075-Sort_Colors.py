from __future__ import annotations


# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        # print(nums)

"""
Do not return anything, modify nums in-place instead.
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
test = Solution()
test.sortColors([2,0,2,1,1,0])
