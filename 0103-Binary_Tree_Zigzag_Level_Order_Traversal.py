from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        sign = 1

        while root and level:
            curNodeVals, nextLevNodes = [], []
            sign *= -1

            for node in level:
                curNodeVals.append(node.val)
                if node.left:
                    nextLevNodes.append(node.left)
                if node.right:
                    nextLevNodes.append(node.right)

            if sign > 0:
                curNodeVals = curNodeVals[::-1]
            ans.append(curNodeVals)
            level = nextLevNodes

        return ans
        # print(ans)


test = Solution()
test.zigzagLevelOrder(TreeNode(3, TreeNode(9),\
                      TreeNode(20, TreeNode(15), TreeNode(7))))
"""
[
  [3],
  [20,9],
  [15,7]
]
"""
