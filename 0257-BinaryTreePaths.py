from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        return [str(root.val) + "->" + v\
                for v in self.binaryTreePaths(root.left)] +\
               [str(root.val) + "->" + v\
                for v in self.binaryTreePaths(root.right)]
