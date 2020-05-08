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
Morris Inorder Tree Traversal
https://www.youtube.com/watch?v=wGXB9OWhPTg
Not required for recursive nor stack
"""

"""
Compare Morris vs regulara Inorder Traversal &
How to find "something wrong" in the node
https://leetcode.com/problems/recover-binary-search-tree/discuss/187407/Python-short-and-slick-solution-(108ms-beats-100)-both-stack-and-Morris-versions

"""

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        curr, prev, drops = root, TreeNode(float('-inf')), []

        while curr:
            if curr.left:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    temp.right, curr = curr, curr.left
                    continue
                temp.right = None
            if curr.val < prev.val:
                drops.append((prev, curr))
            prev, curr = curr, curr.right

        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val


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
root = TreeNode(1,TreeNode(3, None, TreeNode(2)))
test.recoverTree(root)
# TreeNode(3,TreeNode(1, TreeNode(None), TreeNode(2)))
print("------------------------------")
b = BstNode(root)
b.display()
print("------------------------------")


test = Solution()
root = TreeNode(3,TreeNode(1), TreeNode(4, TreeNode(2)))
test.recoverTree(root)
# TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3)))
print("------------------------------")
b = BstNode(root)
b.display()
print("------------------------------")
