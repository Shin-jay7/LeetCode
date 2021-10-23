from __future__ import annotations


class Solution:
    def guessNumber(self, n: int) -> int:
        pick = (n+1) // 2
        while 0 < pick < n+1:
            res = guess(pick)
            if res == 0:
                return pick
            elif res == -1:
                pick -= 1
            else:
                pick += 1
