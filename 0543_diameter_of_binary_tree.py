from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def height(node):
            if not node:
                return -1
            left, right = height(node.left), height(node.right)
            self.ans = max(self.ans, 2 + left + right)
            return 1 + max(left, right)

        height(root)
        return self.ans
