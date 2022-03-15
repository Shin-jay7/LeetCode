from __future__ import annotations
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        return str(root.val) + ' '\
            + self.serialize(root.left)\
            + self.serialize(root.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        deq = deque(int(val) for val in data.split())

        def build_tree(min_val, max_val):
            if deq and min_val < deq[0] < max_val:
                val = deq.popleft()
                return TreeNode(
                     val,
                     build_tree(min_val, val),
                     build_tree(val, max_val)
                    )

        return build_tree(float('-inf'), float('inf'))
