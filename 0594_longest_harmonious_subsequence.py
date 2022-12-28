from __future__ import annotations
from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max((cnt[x] + cnt[x+1] for x in cnt if cnt[x+1]), default=0)
