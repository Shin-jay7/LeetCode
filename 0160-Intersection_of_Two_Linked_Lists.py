from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB
        """
        the idea is if you switch head, the possible difference
        between length would be countered. On the second traversal,
        they either hit or miss.  if they meet, pA or pB would be
        the node we are looking for, if they didn't meet, they will
        hit the end at the same iteration, pa == pb == None
        """
        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
