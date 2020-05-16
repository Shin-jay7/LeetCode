from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False

        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(root.left, sum-root.val) or\
               self.hasPathSum(root.right, sum-root.val)


test = Solution()
test.hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11,\
                TreeNode(7), TreeNode(2))), TreeNode(8,\
                TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22)
# 22
