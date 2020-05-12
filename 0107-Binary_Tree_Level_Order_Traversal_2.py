from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]

        while root and level:
            currNodes, nextLevel = [], []
            for node in level:
                currNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            ans.insert(0, currNodes)
            level = nextLevel

        return ans
        # print(ans)


test = Solution()
test.levelOrderBottom(TreeNode(3, TreeNode(9), TreeNode(20,\
                      TreeNode(15), TreeNode(7))))
"""
[
  [15,7],
  [9,20],
  [3]
]
"""
