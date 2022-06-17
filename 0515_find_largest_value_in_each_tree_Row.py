from __future__ import annotations
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def find_max_in_row(node, depth, maxes):
            if not node:
                return
            if len(maxes) == depth:
                maxes.append(float('-inf'))
            maxes[depth] = max(maxes[depth], node.val)
            find_max_in_row(node.left, depth+1, maxes)
            find_max_in_row(node.right, depth+1, maxes)

        maxes = []
        find_max_in_row(root, 0, maxes)
        return maxes


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        maxes, row = [], [root]
        while any(row):  # Any to deal with the case [None] 
            maxes.append(max(node.val for node in row))
            row = [
                kid for node in row for kid in 
                (node.left, node.right) if kid
            ]

        return maxes


