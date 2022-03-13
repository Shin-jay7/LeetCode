from __future__ import annotations
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
          self, l1: Optional[ListNode], l2: Optional[ListNode]
         ) -> Optional[ListNode]:
        l1_sum, l2_sum = 0, 0
        while l1:
            l1_sum = l1_sum * 10 + l1.val
            l1 = l1.next
        while l2:
            l2_sum = l2_sum*10 + l2.val
            l2 = l2.next
        _sum = l1_sum + l2_sum

        head = ListNode()
        if _sum == 0:
            return head
        while _sum:
            v, _sum = _sum % 10, _sum // 10
            head.next = ListNode(v, head.next)

        return head.next


class Solution:
    def addTwoNumbers(
          self, l1: Optional[ListNode], l2: Optional[ListNode]
         ) -> Optional[ListNode]:
        len1, len2 = self.getLength(l1), self.getLength(l2)
        l1 = self.addLeadingZeros(len2-len1, l1)
        l2 = self.addLeadingZeros(len1-len2, l2)
        upper_digit, ans = self.combineList(l1, l2)
        if upper_digit > 0:
            ans = ListNode(upper_digit, ans)
        return ans

    def getLength(self, node: Optional[ListNode]) -> int:
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def addLeadingZeros(
          self, n: int, node: Optional[ListNode]
         ) -> Optional[ListNode]:
        for i in range(n):
            node = ListNode(0, node)
        return node

    def combineList(
          self, l1: Optional[ListNode], l2: Optional[ListNode]
         ) -> Tuple[int, Optional[ListNode]]:
        if not l1 and not l2:
            return (0, None)
        num, new_node = self.combineList(l1.next, l2.next)
        _sum = l1.val + l2.val + num
        ans = ListNode(_sum % 10, new_node)
        return (_sum // 10, ans)
