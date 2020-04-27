from __future__ import annotations


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1 - obstacleGrid[i][j]
                elif i == 0:
                    obstacleGrid[i][j] =\
                        obstacleGrid[i][j-1] if obstacleGrid[i][j] != 1 else 0
                elif j == 0:
                    obstacleGrid[i][j] =\
                        obstacleGrid[i-1][j] if obstacleGrid[i][j] != 1 else 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]\
                                         if obstacleGrid[i][j] != 1 else 0

        return obstacleGrid[-1][-1]
        # print(obstacleGrid[-1][-1])


test = Solution()
test.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]) # 2

test = Solution()
test.uniquePathsWithObstacles([
  [1]
]) # 0

test = Solution()
test.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,1]
]) # 0

test = Solution()
test.uniquePathsWithObstacles([
  [0,1],
  [1,0]
]) # 0

test = Solution()
test.uniquePathsWithObstacles([
  [1,0]
]) # 0

test = Solution()
test.uniquePathsWithObstacles([
  [0,0],
  [1,1],
  [0,0]
]) # 0
