from __future__ import annotations
from typing import AnyStr, List
from itertools import combinations


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [
            str(h) + ":" + str(m).zfill(2)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count("1") == turnedOn
        ]


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        LED = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        hour, minute, ans = 0, 0, []
        for perm in combinations(range(10), turnedOn):
            for idx in perm:
                if 0 <= idx <= 3:
                    hour += LED[idx]
                elif 4 <= idx <= 9:
                    minute += LED[idx]
            if hour < 12 and minute < 60:
                ans.append(str(hour) + ":" + str(minute).zfill(2))
            hour, minute = 0, 0

        return ans


test = Solution()
test.readBinaryWatch(2)

test = Solution()
test.readBinaryWatch(9)
