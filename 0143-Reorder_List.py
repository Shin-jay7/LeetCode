from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return

        mid = self.getMid(head)
        afterMid = mid.next
        mid.next = None
        tail = self.reverseList(afterMid)

        while head and tail:
            head.next, head = tail, head.next
            tail.next, tail = head, tail.next

    def getMid(self, head: ListNode) -> ListNode:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            head.next, head, prev = prev, head.next, head

        return prev


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return

        # Find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place: Pls note that the last node of "first"
        #                 and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
