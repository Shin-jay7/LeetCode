from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        def swap(begin, end):
            """
            dummy->1->2->3->4->5->6->nil
            begin        end

            =>

            dummy->2->1->3->4->5->6->nil
            begin        end
            """
            p = begin.next
            q = p.next
            while q != end:
                tmp = q.next
                q.next = p
                p = q
                q = tmp
            begin.next.next = end
            begin.next = p

        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            count = 0
            for _ in range(k):
                if curr:
                    curr = curr.next
                    count += 1
            if count == k:
                swap(prev, curr)
            while prev.next != curr:
                prev = prev.next

        return dummy.next

