from __future__ import annotations
from typing import List
from functools import cache
from itertools import product


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        neibs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        @cache
        def dfs(x, y):
            ans = 1
            for dx, dy in neibs:
                if 0 <= x+dx < m and 0 <= y+dy < n and\
                   matrix[x+dx][y+dy] < matrix[x][y]:
                    ans = max(ans, dfs(x+dx, y+dy)+1)
            return ans

        return max(dfs(i, j) for i, j in product(range(m), range(n)))
