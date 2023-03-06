from __future__ import annotations
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(
            self, nums: List[int]
    ) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
