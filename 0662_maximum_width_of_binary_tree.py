from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        width, level = 0, [(root, 1)]
        while len(level):
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for item, num in level:
                if item.left:
                    next_level.append((item.left, num*2))
                if item.right:
                    next_level.append((item.right, num*2 + 1))
            level = next_level
        return width


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        width, level = 0, [(root, 1)]
        while level:
            width = max(width, level[-1][1] - level[0][1] + 1)
            next_level = []
            for node, number in level:
                if node.left:
                    next_level.append((node.left, number*2))
                if node.right:
                    next_level.append((node.right, number*2 + 1))
            level = next_level
        return width
