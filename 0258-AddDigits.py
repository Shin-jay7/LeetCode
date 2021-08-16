from __future__ import annotations


class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num-1) % 9 + 1
        # Then numbers n and sum(n) (where by sum(n) we denote 
        # sum of digits of number n) have the same remainder 
        # if we divide them by 9


test = Solution()
test.addDigits(38) # 2

test = Solution()
test.addDigits(0) # 0
