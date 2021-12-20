from __future__ import annotations
from typing import List
from heapq import heappush, heappop


# https://leetcode.com/problems/trapping-rain-water-ii/discuss/1138028/Python3Visualization-BFS-Solution-With-Explanation
class Solution:
    def trapRainWater(self, heightMap: list[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        level, ans = 0, 0

        while heap:
            height, x, y = heappop(heap)
            level = max(height, level)
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heappush(heap, (heightMap[i][j], i, j))
                    if heightMap[i][j] < level:
                        ans += level - heightMap[i][j]
                    heightMap[i][j] = -1  # Set -1 if visited

        print(ans)
        return ans


test = Solution()
test.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]) # 4

test = Solution()
test.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]) 
# 10