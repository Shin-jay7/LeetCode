from __future__ import annotations

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None

        lastElement = head
        length = 1
        while lastElement.next:
            lastElement = lastElement.next
            length += 1

        k %= length

        # The list is now a circular linked list with last node
        # pointing to first node
        lastElement.next = head

        tempNode = head
        for _ in range(length-k-1):
            tempNode = tempNode.next

        ans = tempNode.next
        # Cut the circular
        tempNode.next = None

        return ans

"""
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL

Input: 1->2->NULL, k = 0
Output: 1->2->NULL

"""
