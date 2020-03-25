from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode()
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                # jump : used to connect last node in previous k-group
                # to first node in following k-group
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next
