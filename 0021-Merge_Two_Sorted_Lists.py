from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp_l3 = ListNode()
        l3 = tmp_l3

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        l3.next = l1 if l1 else l2

        return tmp_l3.next
