from __future__ import annotations
from typing import List


class Solution:
    def calPoints(self, operations: List[int]) -> int:
        nums = []
        for op in operations:
            if op == "C":
                nums.pop()
            elif op == "D":
                nums.append(nums[-1]*2)
            elif op == "+":
                nums.append(nums[-1]+nums[-2])
            else:
                nums.append(int(op))
        return sum(nums)
