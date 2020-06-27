from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None

        def getSize(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next

            return cnt

        def split(node, step):
            i = 1
            while i < step and node:
                node = node.next
                i += 1

            if head is None: return None
            temp, node.next = node.next, None

            return temp

        def merge(l, r, node):
            cur = node
            while l and r:
                if l.val < r.val:
                    cur.next, l = l , l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next

            cur.next = l if l is not None else r
            while cur.next is not None:
                cur = cur.next

            return cur

        size = getSize(head)
        bs = 1
        dummy = ListNode()
        dummy.next = head
        l, r, tail = None, None, None

        while bs < size:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1

        return dummy.next


# Recuisive takes o(lgn) space complexity
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(*map(self.sortList, (head, slow)))

    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next
        tail.next = h1 or h2

        return dummy.next
