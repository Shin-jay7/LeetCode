from __future__ import annotations
from typing import List
import random


# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
class Solution:
    def __init__(self, m: int, n: int):
        self.rows, self.cols = m, n
        self.zeros = self.rows * self.cols  # num of remaining 0
        self.swap = {}  # {original index: new index}

    def flip(self) -> List[int]:
        self.zeros -= 1  # flip changes 0 to 1
        idx = random.randint(0, self.zeros)
        cur_idx = idx
        if idx in self.swap:
            cur_idx = self.swap[idx]
        tail_idx = self.zeros
        if tail_idx in self.swap:
            tail_idx = self.swap[tail_idx]
        self.swap[idx] = tail_idx
        return divmod(cur_idx, self.cols)

    def reset(self) -> None:
        self.swap = {}
        self.zeros = self.rows * self.cols
