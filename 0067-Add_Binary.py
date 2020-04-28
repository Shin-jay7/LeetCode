from __future__ import annotations


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            carry, num = divmod(carry, 2)
            ans += str(num)

        return ans[::-1]
        # print(ans[::-1])


test = Solution()
test.addBinary("11", "1") # "100"

test = Solution()
test.addBinary("1", "11") # "100"

test = Solution()
test.addBinary("1010", "1011") # "10101"
