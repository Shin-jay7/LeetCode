from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def _display_aux(self):
        # Returns list of strings, width, height, and horizontal
        # coordinate of the root.

        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2

            return [line], width, height, middle

        # Only left child
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x+1) * ' ' + (n-x-1) * '_' + s
            second_line = x * ' ' + '/' + (n-x-1+u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]

            return [first_line, second_line] +\
                    shifted_lines, n + u, p + 2, n + u // 2

        # Only right child
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n-x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n-x-1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]

            return [first_line, second_line] +\
                    shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x+1) * ' ' + (n-x-1) * '_' + s + y * '_' + (m-y) * ' '
        second_line = x * ' ' + '/' + (n-x-1+u+y) * ' ' + '\\' + (m-y-1) * ' '
        if p < q:
            left += [n * ' '] * (q-p)
        elif q < p:
            right += [m * ' '] * (p-q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] +\
                [a + u * ' ' + b for a,b in zipped_lines]

        return lines, n + m + u, max(p, q) + 2, n + u // 2


"""
DFS Postorder vs DFS Preorder vs DFS Inorder vs BFS
https://leetcode.com/problems/validate-binary-search-tree/Figures/145_transverse.png
"""

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int])\
                  -> TreeNode:
        preorder = deque(preorder)

        return self.getTree(preorder, inorder)

    def getTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])
            root.left = self.getTree(preorder, inorder[:idx])
            root.right = self.getTree(preorder, inorder[idx+1:])

            return root


class BstNode:
    def __init__(self, node):
        self.node = node
        self.val = node.val
        self.right = node.right
        self.left = node.left

    def display(self):
        lines, _, _, _ = self.node._display_aux()
        for line in lines:
            print(line)


test = Solution()
ans = test.buildTree([3,9,20,15,7], [9,3,15,20,7])
print("------------------------------")
b = BstNode(ans)
b.display()
print("------------------------------")
"""
------------------------------
 3___
/    \
9   20
   /  \
  15  7
------------------------------
"""


