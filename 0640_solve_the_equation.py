from __future__ import annotations
import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate(expression):
            tokens = expression.\
                     replace("+", "#+").replace("-", "#-").split("#")
            print(tokens)
            ans = [0] * 2
            for token in tokens:
                if not token:
                    continue
                if token == "x" or token == "+x":
                    ans[0] += 1
                elif token == "-x":
                    ans[0] -= 1
                elif "x" in token:
                    ans[0] += int(token[:token.index("x")])
                else:
                    ans[1] += int(token)
            return ans
        parts = equation.split("=")
        left = evaluate(parts[0])
        right = evaluate(parts[1])
        a = left[0] - right[0]
        b = right[1] - left[1]
        if a == 0 and b == 0:
            return "Infinite solutions"
        if a == 0:
            return "No solution"
        return "x={}".format(b // a)


class Solution:
    def solveEquation(self, equation: str) -> str:
        x = a = 0
        side = 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                x += side * int(sign + '1') * int(num or 1)
            elif num:
                a -= side * int(sign + num)
        return 'x=%d' % (a // x)\
               if x else "No solution" if a else "Infinite solutions"


class Solution:
    def solveEquation(self, equation: str) -> str:
        z = eval(equation.
                 replace('x', 'j').replace('=', '-(') + ')', {'j': 1j})
        a, x = z.real, -z.imag
        return 'x=%d' % (a // x)\
               if x else "No solution" if a else "Infinite solutions"


test = Solution()
test.solveEquation("x+5-3+x=6+x-2")  # "x=2"

test = Solution()
test.solveEquation("x=x")  # "Infinite solutions"

test = Solution()
test.solveEquation("2x=x")  # "x=0"
