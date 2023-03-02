from __future__ import annotations
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_idxes = deque(idx for idx, cha in enumerate(senate) if cha == "R")
        d_idxes = deque(idx for idx, cha in enumerate(senate) if cha == "D")
        while r_idxes and d_idxes:
            r_idx, d_idx = r_idxes.popleft(), d_idxes.popleft()
            if r_idx < d_idx:
                r_idxes += r_idx + len(senate)
            else:
                d_idxes += d_idx + len(senate)
        return r_idxes and "Radinat" or "Dire"
