from __future__ import annotations


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        # Always stack min so far and value
        if self.stack:
            self.stack.append(min(self.stack[-2], x))
        else:
            self.stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-2]


test = MinStack()
test.push(-2)
test.push(0)
test.push(-3)
test.getMin() # -3
test.pop()
test.top() # 0
test.getMin() # -2
