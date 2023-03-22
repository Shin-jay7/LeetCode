from __future__ import annotations


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # n/presses 0 1 2 3 4 5
        # 0         1 1 1 1 1 1
        # 1         1 2 2 2 2 2
        # 2         1 3 4 4 4 4
        # 3         1 4 7 8 8 8
        # 4         1 4 7 8 8 8
        # 5         1 4 7 8 8 8
        def fn(n, presses):
            if presses * n == 0:
                return 1
            return fn(n-1, presses) + fn(n-1, presses-1)
        return fn(min(n, 3), min(presses, 3))
