from __future__ import annotations


# 1221121221221121122
# Use num = 3 - num to flip between 1 and 2
class Solution:
    def magicalString(self, n: int) -> int:
        S, idx = [1, 2, 2], 2
        while len(S) < n:
            S += [3 - S[-1]] * S[idx]
            idx += 1
        return S[:n].count(1)
