from __future__ import annotations
from typing import List
from collections import deque


# Time limit exceeded
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        m, n = len(forest), len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        ans = 0
        pos_i, pos_j = 0, 0
        for _, tree_i, tree_j in trees:
            step = self.BFS(forest, pos_i, pos_j, tree_i, tree_j)
            if step == -1:
                return -1
            else:
                ans += step
                forest[tree_i][tree_j] = 1
                pos_i, pos_j = tree_i, tree_j
        return ans

    def BFS(self, forest, pos_i, pos_j, tree_i, tree_j):
        m, n = len(forest), len(forest[0])
        visited, queue, step = set(), deque(), -1
        queue.append((pos_i, pos_j))
        while len(queue) > 0:
            step += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                visited.add((i, j))
                if i == tree_i and j == tree_j:
                    return step
                for move_i, move_j in [
                     (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if move_i < 0 or move_i >= m or\
                       move_j < 0 or move_j >= n or\
                       forest[move_i][move_j] == 0 or\
                       (move_i, move_j) in visited:
                        continue
                    queue.append((move_i, move_j))
        return -1


# Hadlock's algorithm
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        trees = [(height, i, j)
                 for i, row in enumerate(forest)
                 for j, height in enumerate(row)
                 if height > 1]

        queue, reachable = [(0, 0)], set()
        for i, j in queue:
            if (i, j) not in reachable and forest[i][j]:
                reachable.add((i, j))
                queue.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
        if not all((i, j) in reachable for _, i, j in trees):
            return -1

        def distance(cur_i, cur_j, next_i, next_j):
            queue, visited = [(cur_i, cur_j, 0)], set()
            for cur_i, cur_j, distance in queue:
                if (cur_i, cur_j) not in visited and forest[cur_i][cur_j]:
                    visited.add((cur_i, cur_j))
                    if cur_i == next_i and cur_j == next_j:
                        return distance
                    queue.extend(
                        [(cur_i+1, cur_j, distance+1),
                         (cur_i-1, cur_j, distance+1),
                         (cur_i, cur_j+1, distance+1),
                         (cur_i, cur_j-1, distance+1)])
            return -1

        trees.sort()
        return sum(
            distance(cur_i, cur_j, next_i, next_j)
            for (_, cur_i, cur_j), (_, next_i, next_j)
            in zip([(0, 0, 0)]+trees, trees))
