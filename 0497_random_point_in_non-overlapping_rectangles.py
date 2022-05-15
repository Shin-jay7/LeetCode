from __future__ import annotations
from typing import List
from itertools import accumulate
import random
import bisect


class Solution:
    def __init__(self, rects: List[List[int]]):
        w = [(x2-x1+1) * (y2-y1+1) for x1, y1, x2, y2 in rects]
        self.weights = [acc / sum(w) for acc in accumulate(w)]
        self.rects = rects

    def pick(self) -> List[int]:
        idx = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]
