from __future__ import annotations
from typing import List
import random


class Solution:
    def __init__(self, n: int, blacklist: List[int]) -> None:
        blacklist = set(blacklist)
        self.n = n - len(blacklist)
        k = [k for k in blacklist if k < self.n]
        v = [v for v in range(self.n, n) if v not in blacklist]
        self.mapping = dict(zip(k, v))

    def pick(self) -> int:
        key = random.randint(0, self.n - 1)
        return self.mapping.get(key, key)


# Time Limit Exceeded
class Solution:
    def __init__(self, n: int, blacklist: List[int]) -> None:
        for i in range(n):
            if i not in blacklist:
                self.whitelist.append(i)

    def pick(self) -> int:
        return self.whitelist[random.randint(0, len(self.whitelist) - 1)]
