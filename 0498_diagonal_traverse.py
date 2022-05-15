from __future__ import annotations
from typing import List
from collections import defaultdict


# Please notice sum of row & col indices in the same diagonal is same.
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                diagonals[i+j].append(mat[i][j])
        ans = []
        for d in diagonals.items():
            if d[0] % 2:
                ans.extend(d[1])
            else:
                ans.extend(d[1][::-1])
        return ans


test = Solution()
test.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])  #  [1,2,4,7,5,3,6,8,9]
