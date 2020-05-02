from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = linkedList.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode()
        after = after_head = ListNode()

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next


test = Solution()
ans  = test.partition(\
            ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5,\
            ListNode(2)))))), 3)
linkedList = SinglyLinkedList()
linkedList.add(ans)
print([node.val for node in linkedList])
# [1, 2, 2, 4, 3, 5]
