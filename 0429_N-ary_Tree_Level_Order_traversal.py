from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        queue = [root] if root else []
        while queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return ans


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(node, level):
            if not node:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(node.val)
            for child in node.children:
                dfs(child, level+1)

        ans = []
        dfs(root, 0)
        return ans
