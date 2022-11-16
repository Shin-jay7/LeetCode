from __future__ import annotations
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(set(candyType)))
