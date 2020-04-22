from __future__ import annotations


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[""]*n for _ in range(n)]
        left, right, top, down, num = 0, n-1, 0, n-1, 1

        while left <= right and top <= down:
            for _ in range(left, right+1):
                ans[top][_] = num
                num += 1
            top += 1

            for _ in range(top, down+1):
                ans[_][right] = num
                num += 1
            right -= 1

            for _ in range(right, left-1, -1):
                ans[down][_] = num
                num += 1
            down -= 1

            for _ in range(down, top-1, -1):
                ans[_][left] = num
                num += 1
            left += 1

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
