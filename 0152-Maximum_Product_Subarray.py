from __future__ import annotations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)
        l, r = 0, 1
        subMax, totalMax = nums[0], nums[0]

        while l < n-1 and r < n:
            acc = nums[l]
            while r < n:
                acc *= nums[r]
                subMax = max(subMax, acc)
                r += 1
            l += 1
            r = l+1
            totalMax = max(totalMax, subMax)
            subMax = nums[l]

        return max(totalMax, subMax)
        # print(max(totalMax, subMax))


test = Solution()
test.maxProduct([-2,3,-4]) # 24

test = Solution()
test.maxProduct([0,2]) # 2

test = Solution()
test.maxProduct([-3,-1,-1]) # 3

test = Solution()
test.maxProduct([2,3,-2,4]) # 6

test = Solution()
test.maxProduct([-2,0,-1]) # 0

test = Solution()
test.maxProduct([1]) # 1

test = Solution()
test.maxProduct([]) # 0
