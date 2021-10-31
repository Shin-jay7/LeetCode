from __future__ import annotations
from typing import Optional
from random import choice, random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.vals)


# https://florian.github.io/reservoir-sampling/
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # nodes are number of nodes we count in list so far
        # and cur is current node we are in.
        nodes, cur = 1, 1
        head, ans = self.head, self.head
        while head.next:
            nodes += 1
            head = head.next
            if random() < cur/nodes:
                ans = ans.next
                cur += 1

        return ans.val
