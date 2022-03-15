from __future__ import annotations
from collections import defaultdict
from typing import List


# Suppose we have three points A1, A2, A3 all have the same distence
# to point B. Then our output should be
# [B, A1, A2]
# [B, A1, A3]
# [B, A2, A1]
# [B, A2, A3]
# [B, A3, A1]
# [B, A3, A2]
# You need to permutate 3 points into 2 positions.
# P(n, r) = n! / (n-r)! = 3! / (3-2)! = 3*2*1 / 1 = 6
# When you permutate x points into 2 positions.
# P(x, 2) = x(x-1)
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            dist_map = defaultdict(int)
            for q in points:
                dist = pow(p[0]-q[0], 2) + pow(p[1]-q[1], 2)
                dist_map[dist] += 1
            for dist in dist_map:
                ans += dist_map[dist] * (dist_map[dist] - 1)
        
        return ans
