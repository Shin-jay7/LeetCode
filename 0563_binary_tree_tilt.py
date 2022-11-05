from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def tilt(node):
            if not node:
                return 0
            left = tilt(node.left)
            right = tilt(node.right)
            self.ans += abs(left - right)
            return node.val + left + right

        tilt(root)
        return self.ans
