from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []

        ans, valList = [], []

        def listSum(node, sum_, valList):
            sumList = []
            sumList.extend(valList)
            sumList.append(node.val)
            temp = valList
            if not node.left and not node.right:
                if node.val == sum_:
                    ans.append(sumList)
                return
            if node.left:
                listSum(node.left, sum_-node.val, sumList)
            if node.right:
                listSum(node.right, sum_-node.val, sumList)

        listSum(root, sum, valList)

        return ans
        # print(ans)


test = Solution()
test.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),\
             TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),\
             22)
"""
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
