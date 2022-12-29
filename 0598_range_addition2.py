from __future__ import annotations
from typing import List
from operator import mul
import numpy as np
from functools import reduce


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m * n


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return ops and reduce(lambda x, y: min(x) * min(y), zip(*ops)) or m * n


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return mul(*map(min, zip(*ops))) if ops else m * n


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return np.prod(np.min(ops, axis=0)) if ops else m * n


