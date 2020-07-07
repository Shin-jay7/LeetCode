from __future__ import annotations


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)
test.getMin() # -3
test.pop()
test.top() # 0
test.getMin() # -2
