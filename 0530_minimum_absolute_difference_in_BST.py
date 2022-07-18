from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        val_list = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            val_list.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return min(b-a for a, b in zip(val_list, val_list[1:]))


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def calc(node, lo, hi):
            if not node:
                return hi - lo
            left = calc(node.left, lo, node.val)
            right = calc(node.right, node.val, hi)
            return min(left, right)

        return calc(root, float('-inf'), float('inf'))
