from __future__ import annotations
from typing import List


class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
