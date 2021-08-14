from __future__ import annotations


class TreeNode:
    def __init__(self, int: x) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        if root in (None, p, q):
            return root

        left, right =\
            self.lowestCommonAncestor(root.left, p, q),\
            self.lowestCommonAncestor(root.right, p, q)

        return root if left and right else left or right
        # if both children returned a node, means
        # both p and q found so parent is LCA
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
        