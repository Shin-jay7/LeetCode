from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False

        level = [(root, root.val)]

        while level:
            nextLevel = []
            for node in level:
                left, right = node[0].left, node[0].right
                if left:
                    nextLevel.append((left, node[1]+left.val))
                if right:
                    nextLevel.append((right, node[1]+right.val))
                if not left and not right and node[1] == sum:
                    return True
            level = nextLevel

        return False


test = Solution()
test.hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11,\
                TreeNode(7), TreeNode(2))), TreeNode(8,\
                TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22)
# 22
