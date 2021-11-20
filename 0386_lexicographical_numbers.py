from __future__ import annotations
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(list(range(1, n+1)), key=str)


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            # next lexical order of "x" is "x0"
            # otherwise, "x+1"
            new = ans[-1] * 10
            while new > n:
                new //= 10
                new += 1
                while new % 10 == 0:
                    new //= 10
            ans.append(new)

        return ans
