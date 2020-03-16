from __future__ import annotations
import sys


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        min_, total, ans = sys.maxsize, 0, 0

        for i in range(length-2):
            l = i+1
            r = length-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = abs(target - total)

                if min_ > diff:
                    min_ = diff
                    ans = total

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    # print(total)
                    # return
                    return total

        return ans
        # print(ans)

test = Solution()
test.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82) # 82

test = Solution()
test.threeSumClosest([1, 1, 1, 0], 100) # 3

test = Solution()
test.threeSumClosest([1, 1, 1, 0], -100) # 2

test = Solution()
test.threeSumClosest([-1, 2, 1, -4], 1) # 2

test = Solution()
test.threeSumClosest([], 1) # 0

test = Solution()
test.threeSumClosest([0], 1) # 0
