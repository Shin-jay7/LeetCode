from __future__ import annotations


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        prev = n

        while n != 1:
            if n % 2 == 0:
                n //= 2
            if n % 3 == 0:
                n //= 3
            if n % 5 == 0:
                n //= 5

            if n == prev:
                return False
            else:
                prev = n
        
        return True


test = Solution()
test.isUgly(6) # True
