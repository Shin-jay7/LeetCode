from __future__ import annotations

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        digits = []
        for digit in num:
            while k and digits and digits[-1] > digit:
                digits.pop()
                k -= 1
            digits.append(digit)

        return "".join(digits[:-k or None]).lstrip("0") or "0"
