from __future__ import annotations
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev, max_cnt, cur_cnt, ans = None, 0, 0, []

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        if node.val != self.prev:
            self.cur_cnt = 1
        else:
            self.cur_cnt += 1
        if self.cur_cnt == self.max_cnt:
            self.ans.append(node.val)
        elif self.cur_cnt > self.max_cnt:
            self.ans = [node.val]
            self.max_cnt = self.cur_cnt
        self.prev = node.val
        self.dfs(node.right)
