from __future__ import annotations
from typing import List
from itertools import product


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        ans = [[0]*cols for _ in range(rows)]
        dirs = [*product([-1,0,1], repeat=2)]
        for row in range(rows):
            for col in range(cols):
                cells = [img[row+i][col+j] for i,j in dirs
                         if 0 <= row+i < rows and 0 <= col+j < cols]
                ans[row][col] = sum(cells) // len(cells)
        return ans
