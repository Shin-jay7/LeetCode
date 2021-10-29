from __future__ import annotations
from typing import List
from heapq import heappop, heappush
from math import inf


# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1322101/C%2B%2BJavaPython-MaxHeap-MinHeap-Binary-Search-Picture-Explain-Clean-and-Concise
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_heap = []
        for r in range(m):
            for c in range(n):
                heappush(max_heap, -matrix[r][c])
                if len(max_heap) > k:
                    heappop(max_heap)

        return -heappop(max_heap)


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        min_heap = []
        for r in range(min(k, m)):
            heappush(min_heap, (matrix[r][0], r, 0))
        ans = -inf
        for i in range(k):
            ans, r, c = heappop(min_heap)
            if c+1 < n:
                heappush(min_heap, (matrix[r][c+1], r, c+1))

        return ans
