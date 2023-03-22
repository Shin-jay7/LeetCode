from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        if root.left and root.right:
            if root.left.val == root.right.val:
                left = self.findSecondMinimumValue(root.left)
                right = self.findSecondMinimumValue(root.right)
                if left == -1:
                    return right
                elif right == -1:
                    return left
                else:
                    return min(left, right)
            elif root.left.val < root.right.val:
                left = self.findSecondMinimumValue(root.left)
                if left == -1:
                    return root.right.val
                else:
                    return min(left, root.right.val)
            else:
                right = self.findSecondMinimumValue(root.right)
                if right == -1:
                    return root.left.val
                else:
                    return min(right, root.left.val)
        else:
            return -1


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        root_val = root.val
        self.ans = float('inf')

        def dfs(node):
            if node:
                if root_val < node.val < self.ans:
                    self.ans = node.val
                if root_val == node.val:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1
