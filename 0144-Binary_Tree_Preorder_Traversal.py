from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
DFS Postorder vs DFS Preorder vs DFS Inorder vs BFS
https://leetcode.com/problems/validate-binary-search-tree/Figures/145_transverse.png
"""

# recursively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.dfs(root, ans)

        return ans

    def dfs(self, node, ans):
        if node:
            ans.append(node.val)
            self.dfs(node.left, ans)
            self.dfs(node.right, ans)


# iteratively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [root], []

        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return ans


test = Solution()
test.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3), None)))
# [1,2,3]
