from __future__ import annotations


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans, prev = 10, 9
        for i in range(1, n):
            prev *= 10-i # ユニークにするには同じ数字を2回使えないので選択肢が減る
            ans += prev

        return n and ans or 1
