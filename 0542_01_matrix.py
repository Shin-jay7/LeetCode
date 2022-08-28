from __future__ import annotations
from typing import List
from collections import deque
import math


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dirs = [0, 1, 0, -1, 0]
        q = deque([])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col))
                else:
                    mat[row][col] = -1

        while q:
            row, col = q.popleft()
            for i in range(4):
                next_row, next_col = row + dirs[i], col + dirs[i+1]
                if next_row < 0 or next_row == rows or\
                   next_col < 0 or next_col == cols or\
                   mat[next_row][next_col] != -1:
                    continue
                mat[next_row][next_col] = mat[row][col] + 1
                q.append((next_row, next_col))

        return mat


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] > 0:
                    top = mat[row-1][col] if row > 0 else math.inf
                    left = mat[row][col-1] if col > 0 else math.inf
                    mat[row][col] = min(top, left) + 1

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if mat[row][col] > 0:
                    bottom = mat[row+1][col] if row < rows-1 else math.inf
                    right = mat[row][col+1] if col < cols-1 else math.inf
                    mat[row][col] = min(mat[row][col], bottom+1, right+1)

        return mat


test = Solution()
test.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])  # [[0,0,0],[0,1,0],[0,0,0]]

test = Solution()
test.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) # [[0,0,0],[0,1,0],[1,2,1]]
