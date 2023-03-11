from __future__ import annotations
from typing import List
from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnts, ends = Counter(nums), Counter()
        for num in nums:
            if not cnts[num]:
                continue
            cnts[num] -= 1
            if ends[num-1] > 0:
                ends[num-1] -= 1
                ends[num] += 1
            elif cnts[num+1] and cnts[num+2]:
                cnts[num+1] -= 1
                cnts[num+2] -= 1
                ends[num+2] += 1
            else:
                return False
        return True
