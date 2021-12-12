from __future__ import annotations
from typing import List
from collections import defaultdict
from random import choice


class Solution:
    def __init__(self, nums: List[int]):
        d = defaultdict(list)
        for idx, num in enumerate(nums):
            d[num].append(idx)
        self.nums = d

    def pick(self, target: int) -> int:
        return choice(self.nums[target])
