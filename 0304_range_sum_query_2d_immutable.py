from __future__ import annotations
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            ans += sum(self.matrix[i][col1:col2+1])
        return ans
