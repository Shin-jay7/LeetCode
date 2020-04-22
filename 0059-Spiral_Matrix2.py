from __future__ import annotations


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Start with the empty matrix, add the numbers in reverse order
        until we added the number 1. Always rotate the matrix clockwise
        and add a top row
        """
        ans, low = [], n*n+1

        while low > 1:
            low, high = low - len(ans), low
            ans = [[i for i in range(low, high)]]\
                + [list(j) for j in zip(*ans[::-1])]

        return ans


test = Solution()
test.generateMatrix(3)
"""
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
