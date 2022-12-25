from __future__ import annotations
from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    def validSquare(
        self,
        p1: List[int],
        p2: List[int],
        p3: List[int],
        p4: List[int]
    ) -> bool:
        def distance(p):
            return abs(p[0] - p[1])
        points = (complex(x, y) for x, y in [p1, p2, p3, p4])
        dists = []
        for comb in combinations(points, 2):
            dis = distance(comb)
            if dis:
                dists.append(dis)
            else:
                return False
        return set(Counter(dists).values()) == {4, 2}


test = Solution()
test.validSquare([0, 0], [1, 1], [1, 0], [0, 1])  # True

test = Solution()
test.validSquare([0, 0], [1, 1], [1, 0], [0, 12])  # False

test = Solution()
test.validSquare([1, 0], [-1, 0], [0, 1], [0, -1])  # True

test = Solution()
test.validSquare([0, 0], [0, 1], [0, 1], [0, 0])  # False
