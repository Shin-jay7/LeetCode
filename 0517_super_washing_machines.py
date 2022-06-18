from __future__ import annotations
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total, n = sum(machines), len(machines)
        if total % n:
            return -1
        target, ans, to_right = total // n, 0, 0
        # to_right: num of dresses to pass to the right machine
        # dresses: num of dresses in the machine
        for dresses in machines:
            to_right = dresses + to_right - target
            ans = max(ans, abs(to_right), dresses-target)

        return ans
