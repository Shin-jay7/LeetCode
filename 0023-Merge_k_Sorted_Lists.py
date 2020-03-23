from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = pointer = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for i in sorted(self.nodes):
            pointer.next = ListNode(i)
            pointer = pointer.next

        return head.next
