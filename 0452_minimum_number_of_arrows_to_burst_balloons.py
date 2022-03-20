from __future__ import annotations
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        dup = [points[0][0], points[0][1]]
        arrow = 0
        for i in range(1, len(points)):
            if points[i][0] <= dup[1]:
                if points[i][1] < dup[1]:
                    dup = [points[i][0], points[i][1]]
                else:
                    dup = [points[i][0], dup[1]]
            else:
                arrow += 1
                dup = [points[i][0], points[i][1]]
        arrow += 1

        return arrow


test = Solution()
test.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) # 2

test = Solution()
test.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) # 4

test = Solution()
test.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) # 2

test = Solution()
test.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]])
# 2
