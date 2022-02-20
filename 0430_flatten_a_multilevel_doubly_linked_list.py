from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


#  https://www.youtube.com/watch?v=pjWqjqGDOlw
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        temp = head
        stack = []
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif stack and not head.next:
                head.next = stack.pop()
                head.next.prev = head
            head = head.next

        return temp




class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        stack, order = [head], []
        while stack:
            last = stack.pop()
            order.append(last)
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)

        for i in range(len(order) - 1):
            order[i+1].prev = order[i]
            order[i].next = order[i+1]
            order[i].child = None

        return order[0]
