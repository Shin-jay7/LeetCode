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


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int])\
                  -> TreeNode:

        """
        The previous solution destroys the postorder list
        unnecessarily. If I used that, I'd be surprised by the
        behavior if I noticed the mutation and might wind up
        with a difficult to track down bug.
        Use an index instead of popping.
        """

        def helper(inorder, i_start, i_end, postorder, p_start,\
                   p_end, dic):
            if i_start > i_end or p_start > p_end:
                return None

            root = TreeNode(postorder[p_end])
            idx = dic[root.val]
            idx_delta = idx - i_start
            root.left =\
             helper(inorder, i_start, idx-1,\
                    postorder, p_start, p_start+idx_delta-1, dic)
            root.right =\
             helper(inorder, idx+1, i_end,\
                    postorder, p_start+idx_delta, p_end-1, dic)

            return root

        dic = {}
        for i,n in enumerate(inorder):
            dic[n] = i

        return helper(inorder, 0, len(inorder)-1,\
                      postorder, 0, len(postorder)-1, dic)


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
ans = test.buildTree([9,3,15,20,7], [9,15,7,20,3])
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
