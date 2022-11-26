from __future__ import annotations
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.dfs(root, ans)
        return ans

    def dfs(self, node, ans):
        if node is None:
            return
        ans.append(node.val)
        for child in node.children:
            self.dfs(child, ans)


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack, ans = [root], []
        while stack:
            temp = stack.pop()
            ans.append(temp.val)
            stack.extend(temp.children[::-1])

        return ans
