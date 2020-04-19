from __future__ import annotations


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, start, end, step, max_ = len(nums), 0, nums[0], 1, 0

        while end < n-1:
            step += 1
            for i in range(start,end+1):
                if nums[i]+i >= n-1:
                    # print(True)
                    # return
                    return True
                max_ = max(max_, nums[i]+i)
            start, end = end, max_
            if nums[start] == 0 and start == end:
                # print(False)
                # return
                return False

        # print(True)
        # return
        return True



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

