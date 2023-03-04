from __future__ import annotations
from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        ans, hmap = [], {}

        def recurse(node):
            if node is None:
                return '#'
            path = ','.join(
                [str(node.val), recurse(node.left), recurse(node.right)]
            )
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    ans.append(node)
            else:
                hmap[path] = 1
            return path

        recurse(root)
        return ans


class Solution:
    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        nodes, path_dict = defaultdict(list), defaultdict()

        def recurse(node):
            if node:
                path = path_dict[
                    node.val, recurse(node.left), recurse(node.right)
                    ]
                nodes[path].append(node)
                return path

        path_dict.default_factory = path_dict.__len__
        recurse(root)
        return [node[0] for node in nodes.values() if node[1:]]
