from __future__ import annotations


class Solution:
    def computeArea(
        self,
        ax1: int, ay1: int, ax2: int, ay2: int,
        bx1: int, by1: int, bx2: int, by2: int
    ) -> int:
        a = abs(ax2 - ax1) * abs(ay2 - ay1)
        b = abs(bx2 - bx1) * abs(by2 - by1)
        w = min(ax2, bx2) - max(ax1, bx1)
        h = min(ay2, by2) - max(ay1, by1)
        
        if w <= 0 or h <= 0:
            return a + b
        else:
            return a + b - w * h


test = Solution()
test.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) # 45

test = Solution()
test.computeArea(-2, -2, 2, 2, -2, -2, 2, 2) # 16

test = Solution()
test.computeArea(0, 0, 0, 0, -1, -1, 1, 1) # 4

test = Solution()
test.computeArea(-2, -2, 2, 2, 3, 3, 4, 4) # 17

test = Solution()
test.computeArea(-2, -2, 2, 2, -2, -2, 2, 2) # 16

test = Solution()
test.computeArea(-2, -2, 2, 2, -1, -1, 1, 1) # 16
