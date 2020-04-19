from __future__ import annotations


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i]+i >= pos:
                pos = i

        # print(pos==0)
        return pos == 0


test = Solution()
test.canJump([1,1,2,2,0,1,1]) # True

test = Solution()
test.canJump([2,0]) # True

test = Solution()
test.canJump([1,2]) # True

test = Solution()
test.canJump([1]) # True

test = Solution()
test.canJump([0]) # True

test = Solution()
test.canJump([2,3,1,1,4]) # True

test = Solution()
test.canJump([3,2,1,0,4]) # False

