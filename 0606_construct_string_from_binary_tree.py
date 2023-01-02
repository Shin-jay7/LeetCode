from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string = str(root.val)
        if root.left:
            string += "(" + self.trees2tr(root.left) + ")"
        if root.right:
            if not root.left:
                # Add empty () to make difference between
                # "1(2)" and "1(()(2))" clear
                string += "()"
            string += "(" + self.tree2str(root.right) + ")"
        return string


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        left = '({})'.format(self.tree2str(root.left))\
               if (root.left or root.right) else ''
        right = '({})'.format(self.tree2str(root.right))\
                if root.right else ''
        return '{}{}{}'.format(root.val, left, right)
