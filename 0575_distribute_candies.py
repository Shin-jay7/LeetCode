from __future__ import annotations
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies, variety = len(candyType)//2, len(set(candyType))
        return variety if variety <= candies else candies
