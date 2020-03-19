from __future__ import annotations

# Reference: https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head

        while first != None:
            length += 1
            first = first.next

        length -= n
        first = dummy

        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next

        return dummy.next


test = Solution()
test.removeNthFromEnd([1,2,3,4,5], 2) # [1,2,3,5]
