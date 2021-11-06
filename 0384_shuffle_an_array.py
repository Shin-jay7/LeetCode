from __future__ import annotations
from typing import List
from random import randint, sample, shuffle


# Fisher-Tates algorithm
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n-1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


class Solution:
    def __init__(self, nums: List[int]):
        self.reset = lambda: nums
        self.shuffle = lambda: sample(nums, len(nums))


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        num = self.nums[:]
        shuffle(num)
        return num
