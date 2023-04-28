from __future__ import annotations
import re


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = str(bin(n))
        if '00' in n or '11' in n:
            return False
        return True


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if re.search(r'00|11', str(bin(n))):
            return False
        return True


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = n ^ (n >> 1)
        return not(bits & (bits+1))


test = Solution()
test.hasAlternatingBits(5) # True

test = Solution()
test.hasAlternatingBits(7) # False
