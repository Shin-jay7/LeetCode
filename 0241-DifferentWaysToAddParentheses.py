from __future__ import annotations


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [eval(expression)]

        ans = []

        for i, s in enumerate(expression):
            if s in "+-*":
                l = self.diffWaysToCompute(expression[:i])
                r = self.diffWaysToCompute(expression[i+1:])
                ans.extend(self.compute(l, r, s))

        return ans

    def compute(self, l, r, op):
        return [eval(str(m)+op+str(n)) for m in l for n in r]
