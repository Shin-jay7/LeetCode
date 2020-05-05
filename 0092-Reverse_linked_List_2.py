from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.newTailInReversed = None

    def __iter__(self):
        node = linkedList.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.newTailInReversed.next = node
        else:
            self.head = node
        self.newTailInReversed = node

"""
Execution speed
Solution2 -> Solution3 -> Solution1
"""


# Solution1
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            # https://stackoverflow.com/questions/1261875/python-nonlocal-statement
            nonlocal left, stop

            if n == 1: return
            right = right.next
            if m > 1: left =left.next

            recurseAndReverse(right, m-1, n-1)

            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next

        recurseAndReverse(right, m, n)

        return head


# Solution2
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return None

        curr, prev = head, None

        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m-1, n-1
        # curr reaches m position

        newTailInReversed, connectorWithReversed = curr, prev

        # Create reversed linked list
        while n:
            next_ = curr.next
            curr.next = prev # turn arrow to left
            prev = curr
            curr = next_
            n -= 1

        # Turn reversed list and connect with before lists
        if connectorWithReversed:
            connectorWithReversed.next = prev
        else:
            head = prev
        # Connect with after list
        newTailInReversed.next = curr

        return head



# Solution3
"""
find linkedlist [m, n], reverse it, then connect m with n+1,
connect n with m-1
"""
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        p = dummy = ListNode()
        dummy.next = head

        for _ in range(m-1):
            p = p.next

        cur = p.next
        pre = None

        for _ in range(n-m+1):
            cur.next, pre, cur = pre, cur, cur.next

        p.next.next = cur
        p.next = pre

        return dummy.next


test = Solution()
ans = test.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4,\
                          ListNode(5, ListNode(None)))))), 2, 4)
linkedList = SinglyLinkedList()
linkedList.add(ans)
print([node.val for node in linkedList])
# [1,4,3,2,5,NULL]
