class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p, q, current, carry = l1, l2, dummyHead, 0

        while p or q or carry:
            x = 0 if p == None else p.val
            y = 0 if q == None else q.val
            sum_ = x + y + carry
            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)
            current = current.next
            if p:
                p = p.next
            if q:
                q = q.next

        return dummyHead.next
