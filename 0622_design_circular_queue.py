from __future__ import annotations


class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.queue):
            self.queue = self.queue[1:]
            return True
        return False

    def Front(self) -> int:
        if len(self.queue):
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if len(self.queue):
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.k


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