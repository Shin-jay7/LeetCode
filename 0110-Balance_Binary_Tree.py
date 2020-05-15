from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None: return True

        def checkBalance(node):
            if node is None: return 0

            left = checkBalance(node.left)
            if left == -1: return -1

            right = checkBalance(node.right)
            if right == -1: return -1

            if abs(left-right) > 1: return -1

            return 1+max(left, right)

        return checkBalance(root) != -1
        # print(checkBalance(root) != -1)


test = Solution()
test.isBalanced(TreeNode(3, TreeNode(9),\
                TreeNode(20, TreeNode(15), TreeNode(7)))) # True

test = Solution()
test.isBalanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4),\
                TreeNode(4)), TreeNode(3)), TreeNode(2))) # False
