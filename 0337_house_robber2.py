from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            L = dfs(node.left)
            R = dfs(node.right)
            return [node.val + L[1] + R[1], max(L) + max(R)]
            # if we rob given node, we cannot rob children
            # if we do not rob given node, we can rob max of children

        return max(dfs(root))
