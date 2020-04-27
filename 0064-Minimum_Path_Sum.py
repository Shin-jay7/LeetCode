from __future__ import annotations

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]

        for j in range(1,n):
            grid[0][j] += grid[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

        return grid[-1][-1]
        # print(grid[-1][-1])


test = Solution()
test.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]) # 7

test = Solution()
test.minPathSum([
  [1,2,5],
  [3,2,1]
]) # 6
