from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        depth, level = 0, [root]

        while level:
            depth += 1
            nextLevel = []
            for node in level:
                left, right = node.left, node.right
                if not left and not right:
                    # print(depth)
                    # return
                    return depth
                if left:
                    nextLevel.append(left)
                if right:
                    nextLevel.append(right)
            level = nextLevel

        return depth
        # print(depth)


test = Solution()
test.minDepth(TreeNode(3, TreeNode(9), TreeNode(20,\
              TreeNode(15), TreeNode(7)))) # 2
