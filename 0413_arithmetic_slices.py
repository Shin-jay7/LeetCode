from __future__ import annotations
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return 0

        diff, cnt, arith = nums[1] - nums[0], 1, []
        for i in range(2, length):
            if diff == nums[i] - nums[i-1]:
                cnt += 1
            else:
                if cnt > 1:
                    arith.append(cnt)
                cnt, diff = 1, nums[i] - nums[i-1]
        if cnt > 1:
            arith.append(cnt)

        # Sum of 1...n: 1/2 * n * (n+1)
        # print(sum((a-1) * a // 2 for a in arith))
        return sum((a-1) * a // 2 for a in arith)


test = Solution()
test.numberOfArithmeticSlices([1,2,3,4]) # 3

test = Solution()
test.numberOfArithmeticSlices([1,2,3,8,9,10]) # 2
