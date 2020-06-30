from __future__ import annotations


import operator
operators = { "+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "/": operator.truediv }

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                calc = operators[token](int(operand1), int(operand2))
                stack.append(calc)
            else:
                stack.append(token)

        return int(stack.pop())


test = Solution()
test.evalRPN(["2", "1", "+", "3", "*"]) # 9

test = Solution()
test.evalRPN(["4", "13", "5", "/", "+"]) # 6

test = Solution()
test.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) # 22
