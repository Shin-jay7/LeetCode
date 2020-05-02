from __future__ import annotations


class Solution:
    def maximalRectangle(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        n = len(matrix[0])
        height = [0]*(n+1)
        ans = 0

        for row in matrix:
            """
            Reference: 0084-Largest_Rectangles_in_Histogram.py
            Every row in the matrix is viewed as the ground with some
            buildings on it. The building height is the count of consecutive
            1s from that row to above rows.
            """
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n+1):
                while height[i] < height[stack[-1]]:
                    H = height[stack.pop()]
                    W = i-1-stack[-1]
                    ans = max(ans, H*W)
                stack.append(i)

        return ans
        # print(ans)


test = Solution()
test.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]) # 6
