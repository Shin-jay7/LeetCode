from __future__ import annotations
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow, shoot = 0, float('inf')
        for start, end in sorted(points, reverse=True):
            if shoot > end:
                shoot = start
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
