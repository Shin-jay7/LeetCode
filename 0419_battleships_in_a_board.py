from __future__ import annotations
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        rows, cols, cnt = len(board), len(board[0]), 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X" and\
                   (row == 0 or board[row-1][col] == ".") and\
                   (col == 0 or board[row][col-1] == "."):
                    cnt += 1

        return cnt
