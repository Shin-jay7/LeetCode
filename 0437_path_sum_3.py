from __future__ import annotations
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.num_of_paths = 0
        self.dfs(root, targetSum)
        return self.num_of_paths

    def dfs(self, node, targetSum):
        if node is None:
            return
        self.test(node, targetSum)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)

    def test(self, node, targetSum):
        if node is None:
            return
        if node.val == targetSum:
            self.num_of_paths += 1
        self.test(node.left, targetSum-node.val)
        self.test(node.right, targetSum-node.val)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = {0: 1}
        self.dfs(root, targetSum, 0, cache)
        return self.result

    def dfs(self, root, targetSum, currPathSum, cache):
        if root is None:
            return
        currPathSum += root.val
        oldPathSum = currPathSum - targetSum
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        self.dfs(root.left, targetSum, currPathSum, cache)
        self.dfs(root.right, targetSum, currPathSum, cache)
        cache[currPathSum] -= 1


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result, self.count = 0, defaultdict(int)
        self.count[targetSum] = 1
        self.dfs(root, targetSum, 0)
        return self.result

    def dfs(self, root, targetSum, rootSum):
        if not root:
            return None
        rootSum += root.val
        self.result += self.count[rootSum]
        self.count[rootSum + targetSum] += 1
        self.dfs(root.left, targetSum, rootSum)
        self.dfs(root.right, targetSum, rootSum)
        self.count[rootSum + targetSum] -= 1