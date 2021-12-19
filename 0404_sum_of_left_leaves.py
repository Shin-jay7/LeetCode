from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, isLeft=False):
        if not root:
            return

        if not root.left and not root.right:
            if isLeft:
                self.ans += root.val

        self.dfs(root.left, True)
        self.dfs(root.right, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
