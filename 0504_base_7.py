from __future__ import annotations


class Solution:
    def convertToBase7(self, num: int) -> str:
        n, ans = abs(num), ""
        while n:
            ans = str(n % 7) + ans
            n //= 7

        # print("-" * (num < 0) + ans or "0")
        return "-" * (num < 0) + ans or "0"


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)


test = Solution()
test.convertToBase7(100) # "202"

test = Solution()
test.convertToBase7(-7) # "-10"

test = Solution()
test.convertToBase7(0) # "0"

test = Solution()
test.convertToBase7(-8) # "-11"
