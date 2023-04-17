from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self._max = 0

        def traverse(node, parent_val):
            if not node:
                return 0
            left = traverse(node.left, node.val)
            right = traverse(node.right, node.val)
            self._max = max(self._max, left + right)
            if node.val == parent_val:
                return max(left, right) + 1
            else:
                return 0

        traverse(root, None)
        return self._max
