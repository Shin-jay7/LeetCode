from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        for node in queue:
            if node.right:
                queue += [node.right]
            if node.left:
                queue += [node.left]
            # queue += filter(None, (node.right, node.left))
        return node.val

        
    