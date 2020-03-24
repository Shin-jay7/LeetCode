from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head:ListNode) -> ListNode:
        def swap(l):
            _next = l.next
            l.next = _next.next
            _next.next = l
            l = _next
            return l

        curr = head
        prev = None

        while curr and curr.next:
            curr = swap(curr)
            if prev:
                prev.next = curr
            else:
                head = curr
            prev = curr.next
            curr = curr.next.next

        return head
