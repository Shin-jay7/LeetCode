from __future__ import annotations
from functools import lru_cache

"""
About lru_chache
https://stackoverflow.com/questions/49883177/how-does-lru-cache-from-functools-work

List comprehension is a bit faster than loop approach

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# list comprehension approach
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right

            return node

        @lru_cache(None)
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]

        if n == 0: return []

        return trees(1,n)


# loop approach
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []

        return self.generate(1, n)

    @lru_cache(None)
    def generate(self, first, last):
        trees = []
        for root in range(first, last+1):
            for left in self.generate(first, root-1):
                for right in self.generate(root+1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees += node,

        return trees or [None]


test = Solution()
ans = test.generateTrees(3)
"""
[
  [1,None,3,2],
  [3,2,None,1],
  [3,1,None,None,2],
  [2,1,3],
  [1,None,2,None,3]
]
"""
