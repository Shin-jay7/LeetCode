from __future__ import annotations


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str):
        a, b = map(int, num1[:-1].split("+"))
        c, d = map(int, num2[:-1].split("+"))

        return f'{a * c - b * d}+{a * d + b * c}i'
