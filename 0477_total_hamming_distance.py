from __future__ import annotations
from typing import List
from itertools import combinations


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for pair in combinations(nums, 2):
            dis = pair[0] ^ pair[1]
            ans += bin(dis)[2:].count('1')

        return ans
