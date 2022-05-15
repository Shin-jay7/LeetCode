from __future__ import annotations
from typing import List
from itertools import accumulate
import random
import bisect


class Solution:
    def __init__(self, rects: List[List[int]]):
        w = [(x2-x1+1) * (y2-y1+1) for x1, y1, x2, y2 in rects]
        # You're not actually looking for the area of each rectangle, 
        # you're looking for the number of points in the rectangle that can be returned.
        # For example, the rectangle [0,0,0,0] has 1 point that can be returned, (0,0).
        self.weights = [acc / sum(w) for acc in accumulate(w)]
        self.rects = rects

    def pick(self) -> List[int]:
        idx = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]
