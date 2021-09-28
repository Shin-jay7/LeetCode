from __future__ import annotations
from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(d[i]) == 1)
            s -= leaves
            for leaf in leaves:
                for j in d[leaf]:
                    d[j].remove(leaf)
        
        return list(s)


class Solution:
    def findMinHeightTrees(self, n, edges):
        def dfs_helper(start, n):
            self.dist, self.parent = [-1]*n, [-1]*n
            self.dist[start] = 0
            dfs(start)
            return self.dist.index(max(self.dist))

        def dfs(start):
            for neib in Graph[start]:
                if self.dist[neib] == -1:
                    self.dist[neib] = self.dist[start] + 1
                    self.parent[neib] = start
                    dfs(neib)

        Graph = defaultdict(set)
        for u, v in edges:
            Graph[u].add(v)
            Graph[v].add(u)

        tmp_idx = dfs_helper(0, n)
        index = dfs_helper(tmp_idx, n)

        path = []
        while index != -1:
            path.append(index)
            index = self.parent[index]

        Q = len(path)
        return list(set([path[Q//2], path[(Q-1)//2]]))
        # print(list(set([path[Q//2], path[(Q-1)//2]])))


test = Solution()
test.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) # [1]
