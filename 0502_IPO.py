from __future__ import annotations
from typing import List
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
       ) -> int:
        heap = []
        projects = sorted(zip(capital, profits), key=lambda l: l[0])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
            if heap:
                w -= heappop(heap)

        return w


test = Solution()
test.findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1])
