from __future__ import annotations


class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []

        for char in s:
            if char.isdigit():
                num = 10*num + int(char)
            elif char in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][char == "+"]
            elif char == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif char == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + num*sign
