from __future__ import annotations
from typing import List


class Solution:
    def updateBoard(
         self, board: List[List[str]], click: List[int]) -> List[List[int]]:
        adj = [(-1, 0), (1, 0), (0, 1), (0, -1),
               (1, -1), (1, 1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])

        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] == "M":
                board[i][j] = "X"
            elif board[i][j] == "E":
                mine = sum(
                    board[i+x][j+y] == "M" for x, y in adj
                    if 0 <= i+x < m and 0 <= j+y < n
                 )
                board[i][j] = mine and str(mine) or "B"
                for x, y in adj * (not mine):
                    dfs(board, i+x, j+y)
            return board

        return dfs(board, *click)
