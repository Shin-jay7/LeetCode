from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()

        def check_sum(node):
            if not node:
                return False
            if k - node.val in nums:
                return True
            nums.add(node.val)
            return check_sum(node.left) or check_sum(node.right)

        return check_sum(root)
