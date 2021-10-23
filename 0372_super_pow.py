from __future__ import annotations
from typing import List
from math import pow
from functools import reduce


#  https://leetcode.com/problems/super-pow/discuss/84466/Math-solusion-based-on-Euler's-theorem-power-called-only-ONCE-C%2B%2BJava1-line-Python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return 0 if a % 1337 == 0 else\
            pow(a, reduce(lambda x, y: (x*10 + y) % 1140, b) + 1140, 1337)
