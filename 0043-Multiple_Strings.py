from __future__ import annotations


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(num1+"*"+num2))


test = Solution()
test.multiply("2","3") # "6"

test = Solution()
test.multiply("123","456") # "56088"
