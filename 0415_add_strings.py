from __future__ import annotations


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        digits, ans = 1, 0
        while num1 or num2:
            if num1 and num2:
                ans += (ord(num1.pop()) - ord("0"))*digits + (ord(num2.pop()) - ord("0"))*digits
            elif num1:
                ans += (ord(num1.pop()) - ord("0"))*digits
            else:
                ans += (ord(num2.pop()) - ord("0"))*digits
            digits *= 10

        print(str(ans))
        return str(ans)


test = Solution()
test.addStrings("11", "123") # "134"
