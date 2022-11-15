from __future__ import annotations
from typing import Optional
from hashlib import sha256


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMatch(self, node1, node2):
        if not (node1 and node2):
            return node1 is node2
        return node1.val == node2.val and\
            self.isMatch(node1.left, node2.left) and\
            self.isMatch(node1.right, node2.right)

    def isSubtree(
       self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or\
            self.isSubtree(root.right, subRoot)


class Solution:
    def isSubtree(
       self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def hash_(x):
            S = sha256()
            S.update(x.encode('utf-8') )
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            node.merkle = hash_(
                merkle(node.left) + str(node.val) + merkle(node.right))
            return node.merkle

        merkle(root)
        merkle(subRoot) 

        def dfs(node1, node2):
            if not node1:
                return False
            return node1.merkle == node2.merkle or\
                dfs(node1.left, node2) or dfs(node1.right, node2)

        return dfs(root, subRoot)
