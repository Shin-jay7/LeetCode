from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        head = pointer = ListNode(0)

        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, id(l), l))

        while min_heap:
            val, node_id, node, = heapq.heappop(min_heap)
            pointer.next = node
            pointer = pointer.next
            node = node.next

            if node:
                heapq.heappush(min_heap, (node.val, id(node), node))

        return head.next
