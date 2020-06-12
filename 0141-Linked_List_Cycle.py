from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False


# https://groverlab.org/hnbfpr/2017-06-22-fun-with-sys-getrefcount.html
import sys
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if sys.getrefcount(head) > 4:
                return True
            head = head.next

        return False


import sys
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while sys.getrefcount(head) < 5:
            head = head.next

        return bool(head)
