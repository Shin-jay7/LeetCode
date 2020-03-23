from __future__ import annotations
from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        q = PriorityQueue()
        head = pointer = ListNode(0)

        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            pointer.next = node
            pointer = pointer.next
            node = node.next
            if node:
                q.put(Wrapper(node))

        return head.next
