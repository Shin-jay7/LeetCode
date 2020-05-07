from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def helper(node, lower = float('-inf'), upper = float('inf')):
#             if not node: return True

#             val = node.val

#             if val <= lower or val >= upper:
#                 return False
#             if not helper(node.right, val, upper):
#                 return False
#             if not helper(node.left, lower, val):
#                 return False

#             return True

#         return helper(root)
#         # print(helper(root))


# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root: return True

#         stack = [(root, float('inf'), float('-inf')),]

#         while stack:
#             root, lower, upper = stack.pop()
#             if not root:
#                 continue
#             val = root.val
#             if val <= lower or val >= upper:
#                 return False
#                 # print(False)
#                 # return
#             stack.append((root.right, val, upper))
#             stack.append((root.left, lower, val))

#         return True
#         # print(True)


"""
DFS Postorder vs DFS Preorder vs DFS Inorder vs BFS
https://leetcode.com/problems/validate-binary-search-tree/Figures/145_transverse.png
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal is smaller than
            # the previous one, that's not BST.
            if root.val <= inorder:
                return False
                # print(False)
                # return
            inorder = root.val
            root = root.right

        return True
        # print(True)
        # return


test = Solution()
test.isValidBST(TreeNode(2,TreeNode(1),TreeNode(3))) # True

test = Solution()
test.isValidBST(TreeNode(5, TreeNode(1), TreeNode(4,TreeNode(3),TreeNode(6))))
# False
