from __future__ import annotations


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        digits, ans = 1, 0
        while num1 or num2:
            if num1 and num2:
                ans += int(num1.pop())*digits + int(num2.pop())*digits
            elif num1:
                ans += int(num1.pop())*digits
            else:
                ans += int(num2.pop())*digits
            digits *= 10

        # print(str(ans))
        return str(ans)


test = Solution()
test.addStrings("11", "123") # "134"
