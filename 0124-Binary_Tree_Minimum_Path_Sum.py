from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_ = float('-inf')

        def getMax(node):
            nonlocal max_
            if node is None: return 0

            """
            if sum of child nodes are negative, you don't need to
            calculate the child nodes, so stop there and you gain 0
            """
            gainOnLeft = max(getMax(node.left), 0)
            gainOnRight = max(getMax(node.right), 0)

            curMaxPath = node.val + gainOnLeft + gainOnRight
            max_ = max(max_, curMaxPath)

            return node.val + max(gainOnLeft, gainOnRight)

        getMax(root)

        return max_
        # print(max_)


test = Solution()
test.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) # 6

test = Solution()
test.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20,TreeNode(15),TreeNode(7)))) # 42
