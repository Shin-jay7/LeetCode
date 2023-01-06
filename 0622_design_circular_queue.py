from __future__ import annotations


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.max_size = k
        self.head = 0
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.tail = (self.tail+1) % self.max_size
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head, self.tail = 0, -1
        else:
            self.head = (self.head+1) % self.max_size
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.tail == -1

    def isFull(self) -> bool:
        return not self.isEmpty() and\
               (self.tail+1) % self.max_size == self.head


class ListNode:
    def __init__(self, val: int, nxt: ListNode = None):
        self.val = val
        self.next = nxt


class MyCircularQueue:
    def __init__(self, k: int):
        self.max_size = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = ListNode(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


test = MyCircularQueue(3)
test.enQueue(1)  # True
test.enQueue(2)  # True
test.enQueue(3)  # True
test.enQueue(4)  # False
test.Rear()  # 3
test.isFull()  # True
test.deQueue()
test.enQueue(4)
test.Rear()