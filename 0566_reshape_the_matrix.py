from __future__ import annotations
from typing import List


class Solution:
    def matrixReshape(
       self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_len, col_len = len(mat), len(mat[0])
        if row_len * col_len != r * c:
            return mat
        ans = [[0] * c for _ in range(r)]
        for idx in range(r * c):
            ans[idx // c][idx % c] = mat[idx // col_len][idx % col_len]

        return ans


test = Solution()
test.matrixReshape([[1,2],[3,4]], 1, 4)  # [1,2,3,4]

test = Solution()
test.matrixReshape([[1,2],[3,4],[5,6],[7,8]], 2, 4)  # [[1,2,3,4],[5,6,7,8]]

test = Solution()
test.matrixReshape([[1,2],[3,4]], 2, 4)  # [[1,2][3,4]]
