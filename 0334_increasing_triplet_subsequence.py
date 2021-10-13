from __future__ import annotations
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        subseq = [float("inf")]*2
        for num in nums:
            if num < subseq[0]:
                subseq[0] = num
            if subseq[0] < num < subseq[1]:
                subseq[1] = num
            if num > subseq[1]:
                return True

        return False
        