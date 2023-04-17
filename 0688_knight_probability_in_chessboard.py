from __future__ import annotations
from functools import lru_cache


class Solution:
    def knightProbability(
            self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def dfs(i, j, moves):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            if moves == 0:
                return 1
            on_the_board = 0
            for x, y in [
              (1, 2), (1, -2), (-1, 2), (-1, -2),
              (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                on_the_board += dfs(i+x, j+y, moves-1)
            return on_the_board

        return dfs(row, column, k) / 8**k
