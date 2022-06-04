from __future__ import annotations
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        ans = 1
        for n in range(2, int(math.sqrt(num)) + 1):
            if num % n == 0:
                ans += n + num//n

        return ans == num


test = Solution()
test.checkPerfectNumber(28)  # True
