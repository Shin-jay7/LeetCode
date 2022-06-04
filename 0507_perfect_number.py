from __future__ import annotations
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divisors = set([1])
        for n in range(2, int(math.sqrt(num)) + 1):
            if num % n == 0:
                divisors.add(n)
                divisors.add(num//n)

        # print(divisors)
        # print(num == sum(divisors))
        return num == sum(divisors)


test = Solution()
test.checkPerfectNumber(28)  # True
