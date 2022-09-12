from __future__ import annotations
from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        blocks, max_block = defaultdict(int), 0
        for row in wall:
            acc_bricks = 0
            # don't need to consider far right edge of the wall because
            # you cannot draw a line just along one of the two vertical edges.
            for bricks in row[:-1]:
                acc_bricks += bricks
                blocks[acc_bricks] += 1
                max_block = max(max_block, blocks[acc_bricks])
        return len(wall) - max_block


test = Solution()
test.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]) # 3
