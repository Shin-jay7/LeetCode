from __future__ import annotations
from typing import List
from collections import Counter


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        for row in range(m):
            for col in range(n):
                lives = self.counter(board, row, col)
                if board[row][col] == 0:
                    if lives == 3:
                        board[row][col] = 2
                else:
                    if lives < 2 or lives > 3:
                        board[row][col] = 3

        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0

    def counter(self, board, row, col):
        m, n, cnt = len(board), len(board[0]), 0
        for x in [row-1, row, row+1]:
            for y in [col-1, col, col+1]:
                if 0 <= x < m and 0 <= y < n:
                    cnt += board[x][y] % 2

        return cnt - board[row][col]

                    
class Solution:
    def gameOfLifeInfinite(self, live):
        ctr = Counter((I, J)
                      for i, j in live
                      for I in [i-1, i, i+1]
                      for J in [j-1, j, j+1]
                      if I != i or J != j)
        return {ij for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board: List[List[int]]) -> None:
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)
