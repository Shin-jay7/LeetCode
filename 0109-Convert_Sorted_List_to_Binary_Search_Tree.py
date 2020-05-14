from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

"""
Elements processed in the inorder fashion on a binary search
tree turn out to be sorted in ascending order.
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.findSize(head)

        def convert(left, right):
            nonlocal head
            if left > right: return None

            mid = (left+right) // 2

            left = convert(left, mid-1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid+1, right)

            return node

        return convert(0, size-1)

    def findSize(self, head):
        ptr = head
        cnt = 0
        while ptr:
            ptr = ptr.next
            cnt += 1

        return cnt


test = Solution()
ans = test.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0,\
                           ListNode(5, ListNode(9))))))
print("------------------------------")
b = BstNode(ans)
b.display()
print("------------------------------")
"""
     0_
    /  \
  _-3  9
 /    /
-10   5
"""
