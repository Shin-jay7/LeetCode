from __future__ import annotations


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if not node: return
            nodeCopy = seen[node.val] = Node(node.val)
            nodeCopy.neighbors += (seen[neighbor.val] or dfs(neighbor)\
                                   for neighbor in node.neighbors)
            return nodeCopy

        seen = [None] * 101

        return dfs(node)
        # print(dfs(node))
