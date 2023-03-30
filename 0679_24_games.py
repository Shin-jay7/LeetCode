from __future__ import annotations
from typing import List
import math
from itertools import permutations


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24)
        return any(self.judgePoint24([x] + rest)
                   for a, b, *rest in permutations(cards)
                   for x in {a+b, a-b, a*b, b and a/b})
