from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2

        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = pointer = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l1
                l1 = pointer.next.next
            pointer = pointer.next

        if not l1:
            pointer.next = l2
        else:
            pointer.next = l1

        return head.next
