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
            low, high = low-len(ans), low
            ans = [[i for i in range(low, high)]]\
                + [list(j) for j in zip(*ans[::-1])]

        return ans

        """
        low: 10
        high: 10
        [[]]
        low: 9
        high: 10
        [[9]]
        low: 8
        high: 9
        [[8], [9]]
        low: 6
        high: 8
        [[6, 7], [9, 8]]
        low: 4
        high: 6
        [[4, 5], [9, 6], [8, 7]]
        low: 1
        high: 4
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        """


test = Solution()
test.generateMatrix(3)
"""
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
