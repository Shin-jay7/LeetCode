from __future__ import annotations
from functools import cache
from typing import List
from functools import cache


# dp(left, right, k) means the max points you can earn between boxes
# "left" and "right", 
# with "k" boxes before "left" that have the same color as "left".

# Since (a+b)^2 > a^2 + b^2, where a > 0, b > 0, so it's better to greedy to
# remove all contiguous boxes of the same color, instead of split them.
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(left, right, k):
            if left > right:
                return 0
            # Increase both "left" and "k" if they have consecutive colors
            # with boxes[left]
            while left + 1 <= right and boxes[left] == boxes[left+1]:
                left += 1
                k += 1
            # Remove all boxes which has the same color with boxes[left]
            ans = (k+1) * (k+1) + dp(left+1, right, 0)
            # Try to merge non-contiguous boxes of the same color together
            for i in range(left+1, right+1):
                if boxes[left] == boxes[i]:
                    ans = max(ans, dp(i, right, k+1) + dp(left+1, i-1, 0))
            return ans

        # print(dp(0, len(boxes)-1, 0))
        return dp(0, len(boxes)-1, 0)



test = Solution()
test.removeBoxes([1,3,2,2,2,3,4,3,1]) # 23

test = Solution()
test.removeBoxes([1,1,1]) # 9

test = Solution()
test.removeBoxes([1]) # 1

test = Solution()
test.removeBoxes([1,2,1,2,1]) # 11
