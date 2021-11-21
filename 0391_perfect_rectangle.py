from __future__ import annotations
from typing import List


class Solution:
    # all rectangles will share all corners exactly twice, except the four
    # corners of the final rectangle. Using the set symmetric difference
    # will remove these doubled corners and only leave the four corners of
    # the final rectangle. To handle cases of perfectly overlapping rectangles
    # we also sum the areas of the individual rectangles and compare it to the
    # area of the final rectangle
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners, area = set(), 0
        a, b, c, d = float('inf'), float('inf'), float('-inf'), float('-inf')
     
        for x1, y1, x2, y2 in rectangles:
            if x1 <= a and y1 <= b:
                a, b = x1, y1
            if x2 >= c and y2 >= d:
                c, d = x2, y2
            area += (x2-x1) * (y2-y1)
            # XORは同じものはゼロになるので、被らない４つのコーナーだけ残る
            corners ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}

        return corners == {(a, b), (c, d), (a, d), (c, b)} and\
               area == (c-a) * (d-b)
