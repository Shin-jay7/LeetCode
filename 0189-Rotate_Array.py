from __future__ import annotations


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k:
            k = k%len(nums)
            nums[:] = nums[-k:] + nums[:-k]

        print(nums)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k:
            n = len(nums)
            k, end = k%n, n-1
            self.reverse(nums, 0, end-k)
            self.reverse(nums, end-k+1, end)
            self.reverse(nums, 0, end)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


test = Solution()
test.rotate([1,2,3,4,5,6,7], 3) # [5,6,7,1,2,3,4]

test = Solution()
test.rotate([-1,-100,3,99], 2) # [3,99,-1,-100]