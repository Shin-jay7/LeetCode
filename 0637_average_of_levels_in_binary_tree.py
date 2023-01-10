from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        data = []

        def dfs(node, depth=0):
            if node:
                if len(data) <= depth:
                    data.append([0, 0])
                data[depth][0] += node.val
                data[depth][1] += 1
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        dfs(root)
        return [vals / leaves for vals, leaves in data]
