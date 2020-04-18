from __future__ import annotations


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        # print(matrix)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # print(matrix)

        # print(matrix)
        return matrix


test = Solution()
test.rotate([[1,2,3],[4,5,6],[7,8,9]])
