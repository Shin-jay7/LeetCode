from __future__ import annotations


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        # We can't really delete the node, but we can kinda achieve
        # the same effect by instead removing the next node after
        # copying its data into the node that we were asked to delete.
        node.val = node.next.val
        node.next = node.next.next
