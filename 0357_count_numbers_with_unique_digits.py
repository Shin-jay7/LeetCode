from __future__ import annotations


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cnt = 0
        for i in range(int("1" + "0"*n)):
            if len(str(i)) == len(set(str(i))):
                cnt += 1

        return cnt
