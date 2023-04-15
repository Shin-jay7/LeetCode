from __future__ import annotations
import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = math.ceil(len(b)/len(a))
        for i in range(2):
            if b in a*(times+i):
                # print(times+i)
                return times+i
        return -1


test = Solution()
test.repeatedStringMatch("abcd", "cdabcdab") # 3

test = Solution()
test.repeatedStringMatch("a", "aa") # 2

test = Solution()
test.repeatedStringMatch("aaaaaaaaab", "ba") # 2
