from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Iterative approach is faster than recursive one
"""

# Iteratively
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
                # print(ans)
                # return
            node = stack.pop()
            ans.append(node.val)
            root = node.right


# # Recursively
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         ans = []
#         self.helper(root, ans)

#         return ans
#         # print(ans)

#     def helper(self, root, ans):
#         if root:
#             self.helper(root.left, ans)
#             ans.append(root.val)
#             self.helper(root.right, ans)


test = Solution()
test.inorderTraversal(TreeNode(1, None,\
                      TreeNode(2, TreeNode(3, None, None), None)))
# [1, 3, 2]
