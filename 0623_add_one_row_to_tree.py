from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int)\
                  -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        bfs = deque([root])
        while bfs and depth != 1:
            size = len(bfs)
            depth -= 1
            for _ in range(size):
                curr = bfs.popleft()
                if curr.left:
                    bfs.append(curr.left)
                if curr.right:
                    bfs.append(curr.right)
                if depth == 1:
                    curr.left = TreeNode(val, curr.left, None)
                    curr.right = TreeNode(val, None, curr.right)
        return root


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int)\
                  -> Optional[TreeNode]:
        if not root or depth <= 0:
            return None
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth-1)
            root.right = self.addOneRow(root.right, val, depth-1)
        return root
