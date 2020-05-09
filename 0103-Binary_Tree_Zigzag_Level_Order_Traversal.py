from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        flag = 1

        while root and level:
            curNodeVals, nextLevNodes = [], []

            for node in level:
                if flag > 0:
                    curNodeVals.append(node.val)
                else:
                    curNodeVals = [node.val] + curNodeVals
                if node.left:
                    nextLevNodes.append(node.left)
                if node.right:
                    nextLevNodes.append(node.right)

            ans.append(curNodeVals)
            level = nextLevNodes
            flag *= -1

        return ans
        print(ans)


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
