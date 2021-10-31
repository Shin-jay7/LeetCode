from __future__ import annotations
from random import choice
from collections import defaultdict


class RandomizedCollection:
    def __init__(self):
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.nums.append(val)
            return True
        self.nums.append(val)
        return False

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.nums) if self.nums else []


class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.idxs = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.idxs[val].add(len(self.nums)-1)
        return len(self.idxs[val]) == 1

    def remove(self, val: int) -> bool:
        if self.idxs[val]:
            idx_of_num_to_remove = self.idxs[val].pop()
            last_num_in_list = self.nums[-1]
            self.nums[idx_of_num_to_remove] = last_num_in_list
            if self.idxs[last_num_in_list]:
                self.idxs[last_num_in_list].add(idx_of_num_to_remove)
                self.idxs[last_num_in_list].discard(len(self.nums)-1)
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.nums)
