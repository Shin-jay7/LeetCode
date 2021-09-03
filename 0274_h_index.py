from __future__ import annotations
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(idx < val for idx, val in enumerate(sorted(citations, reverse=True)))
