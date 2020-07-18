from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmostInorder(root)

    def _leftmostInorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        top = self.stack.pop()
        if top.right:
            self._leftmostInorder(top.right)
        return top.val

    def hasNext(self) -> bool:
        return self.stack
