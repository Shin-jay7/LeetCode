from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.val = 0

        def visit(node):
            if node:
                visit(node.right)
                node.val += self.val
                self.val = node.val
                visit(node.left)
        visit(root)
        return root


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            return reverse(node.right) + [node] + reverse(node.left) if node else []
        for a, b in zip(reverse(root), reverse(root)[1:]):
            b.val += a.val
        return root
