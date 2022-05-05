from __future__ import annotations
from typing import List
from itertools import groupby


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(sum(g) for _, g in groupby(nums))
