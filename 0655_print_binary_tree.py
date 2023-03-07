from __future__ import annotations
from typing import List, Optional


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node):
            return 0 if not node else 1 + max(
                get_height(node.left), get_height(node.right)
            )

        def print_tree(node, row, left, right):
            if not node:
                return
            mid = (left+right) // 2
            ans[row][mid] = str(node.val)
            print_tree(node.left, row+1, left, mid-1)
            print_tree(node.right, row+1, mid+1, right)

        height = get_height(root)
        width = 2**height-1
        ans = [[""]*width for _ in range(height)]
        print_tree(root, 0, 0, width-1)
        return ans
