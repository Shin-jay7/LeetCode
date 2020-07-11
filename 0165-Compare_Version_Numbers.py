from __future__ import annotations

from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = map(int, version1.split(".")), map(int, version2.split("."))
        v1, v2 = zip(*zip_longest(v1, v2, fillvalue=0))

        return (0,1,-1)[(v1>v2)-(v1<v2)]


test = Solution()
test.compareVersion("0.1", "1.1") # -1

test = Solution()
test.compareVersion("1.0.1", "1") # 1

test = Solution()
test.compareVersion("7.5.2.4", "7.5.3") # -1

test = Solution()
test.compareVersion("1.01", "1.001") # 0

test = Solution()
test.compareVersion("1.0", "1.0.0") # 0
