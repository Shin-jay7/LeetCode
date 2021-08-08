from __future__ import annotations
import math


class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, "+", []
        s += "+"

        for char in s:
            if char.isdigit():
                num = 10*num + int(char)
            elif char == " ":
                pass
            else:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    op = stack.pop()
                    stack.append((op*num))
                elif sign == "/":
                    op = stack.pop()
                    stack.append(math.trunc(op/num))
                num = 0
                sign = char

        return sum(stack)
        # print(sum(stack))


test = Solution()
test.calculate("3+2*2") # 7

test = Solution()
test.calculate(" 3/2 ") # 1

test = Solution()
test.calculate(" 3+5 / 2 ") # 5
