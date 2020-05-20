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
        cur = pre = Node()
        # cur moves from left to right in the child level nodes
        # pre stays at head position in the child leve

        while root:
            while root:
                cur.next = root.left
                cur = cur.next or cur
                cur.next = root.right
                cur = cur.next or cur
                root = root.next
            root, cur = pre.next, pre

        return ans


test = Solution()
test.connect(Node(1, Node(2, Node(4), Node(5)),\
             Node(3, None, Node(7))))
