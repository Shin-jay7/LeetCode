from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
       ) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            if not root.right:
                return root.left
            # Please notice the above logic also covers the case,
            # "If node does not have any children, 
            # then we just delete it and nothing else to do here."
            if not root.left:
                return root.right
            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                # Replace with val which is smallest-larger
                # than the deleted val
                root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
