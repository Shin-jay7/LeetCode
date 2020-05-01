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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = tail = ListNode()
        dummy.next = ptr = head

        while ptr and ptr.next:
            if ptr.val != ptr.next.val:
                ptr, tail = ptr.next, tail.next
            else:
                x = ptr.val
                while ptr and ptr.val == x:
                    ptr = ptr.next
                tail.next = ptr

        return dummy.next


        # walker = dummy = ListNode()
        # dummy.next = head

        # while walker:
        #     runner = walker.next
        #     while runner and runner.next and runner.val == runner.next.val:
        #         runner = runner.next
        #     if walker.next is runner:
        #         walker = walker.next
        #     else:
        #         walker.next = runner.next

        # return dummy.next


test = Solution()
ans = test.deleteDuplicates(\
ListNode(1,\
         ListNode(2,\
                    ListNode(3,\
                               ListNode(3,\
                                          ListNode(4,\
                                                     ListNode(4,\
                                                                ListNode(5)\
)))))))
linkedList = SinglyLinkedList()
linkedList.add(ans)
print([node.val for node in linkedList])
#  [1, 2, 5]


# test = Solution()
# ans = test.deleteDuplicates(\
# ListNode(1,\
#          ListNode(1,\
#                     ListNode(1,\
#                                ListNode(2,\
#                                           ListNode(3)\
# )))))
# linkedList = SinglyLinkedList()
# linkedList.add(ans)
# print([node.val for node in linkedList])
# [2, 3]


