from __future__ import annotations
from typing import Optional, List
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        def dfs(node):
            if node is None:
                return 0
            _sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[_sum] += 1
            return _sum

        cnt = Counter()
        dfs(root)
        max_cnt = max(cnt.values())
        return [_sum for _sum in cnt if cnt[_sum] == max_cnt]
