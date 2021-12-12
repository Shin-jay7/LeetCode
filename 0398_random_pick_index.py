from __future__ import annotations
from typing import List
from random import choice


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        return choice([idx for idx, val in enumerate(self.nums) if val == target])
