from __future__ import annotations


"""
• A straight forward solution using O(mn) space is probably
  a bad idea.
• A simple improvement uses O(m + n) space, but still not
  the best solution.
• Could you devise a constant space solution?
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        for i in range(m):
            if matrix[i][0] == 0:
                row_zero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                col_zero = True
                break

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0

        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if row_zero:
            for i in range(m):
                matrix[i][0] = 0

        if col_zero:
            for j in range(n):
                matrix[0][j] = 0

        # print(matrix)


test = Solution()
test.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])
"""
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""

test = Solution()
test.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
"""
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""
