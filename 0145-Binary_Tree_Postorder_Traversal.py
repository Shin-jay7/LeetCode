from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, ans = [(root, False)], []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return ans
        # print(ans)


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, preorder = [root], []

        while stack:
            node = stack.pop()
            if node:
                preorder.append(node.val)
                # right first for preorder
                stack.append(node.left)
                stack.append(node.right)

        return preorder[::-1]
        # print(preorder[::-1])


test = Solution()
test.postorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3))))
# [3,2,1]
