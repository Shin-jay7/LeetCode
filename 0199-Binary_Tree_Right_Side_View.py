from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)

        return [root.val] + right + left[len(right):]


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        view = []
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        collect(root, 0)

        return view


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        level = [root] if root else []
        view = []
        while level:
            view.append(level[-1].val),
            level = [child for node in level
                     for child in (node.left, node.right) if child]

        return view
