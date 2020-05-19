from __future__ import annotations


class Node:
    def __init__(self, val: int=0, left: 'Node'=None,\
                 right: 'Node'=None, next: 'Node'=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ans = root

        while root and root.left:
            next = root.left

            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                # ↑ means ↓
                # root.right.next = root.next.left if root.next esle None
                root = root.next

            root = next

        return ans


test = Solution()
test.connect(Node(1, Node(2, Node(4), Node(5)),\
             Node(3, Node(6), Node(7))))
