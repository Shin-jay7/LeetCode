from __future__ import annotations
from typing import List


# https://algorithmist.com/wiki/Monotone_chain_convex_hull
# https://algorithmist.com/wiki/Monotone_chain_convex_hull.py
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, trees), key=lambda x: (x[0], x[1]))

        def sign(o, a, b):
            return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])

        def build(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull += p,
            return hull

        return list(set(build(points) + build(points[::-1])))
