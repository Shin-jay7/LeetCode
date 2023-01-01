from __future__ import annotations


# binary digits : valid number : answer
# x : 0 1 : 2
# xx : 00 01 10 : 3 
# xxx : 000 001 010 100 101 : 5
# xxxx : 0000 0001 0010 0100 0101 1000 1001 1010 : 8
# 
# xxxx : 0xxx + 10xx : 5 + 3 = 8

class Solution:
    def findIntegers(self, n: int) -> int:
        x, y, ans = 1, 2, 0
        n += 1
        while n:
            if n & 1 and n & 2:
                ans = 0
            ans += x * (n & 1)
            n >>= 1
            x, y = y, x + y
        return ans
