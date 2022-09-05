from __future__ import annotations


class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_a, cnt_l = 0, 0
        for cha in s:
            if cha == "L":
                cnt_l += 1
                if cnt_l > 2:
                    return False
            else:
                cnt_l = 0
            if cha == "A":
                cnt_a += 1
                if cnt_a > 1:
                    return False

        return True
