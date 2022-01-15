from __future__ import annotations
from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0 <= dx < rows and 0 <= dy < cols and\
                       (dx, dy) not in visited and\
                       heights[dx][dy] >= heights[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            return visited

        pacific = [(0, i) for i in range(cols)] +\
                  [(i, 0) for i in range(1, rows)]
        atlantic = [(rows-1, i) for i in range(cols)] +\
                   [(i, cols-1) for i in range(rows-1)]

        return bfs(pacific) & bfs(atlantic)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, pacific)
            traverse(row, cols-1, atlantic)

        for col in range(cols):
            traverse(0, col, pacific)
            traverse(rows-1, col, atlantic)

        return list(pacific & atlantic)
