from __future__ import annotations
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1, i = Counter(s1), 0
        while i <= len(s2) - len(s1):
            if s2[i] in counter1:
                counter2 = Counter(s2[i:i+len(s1)])
                if counter1 == counter2:
                    return True
            i += 1
        return False


test = Solution()
test.checkInclusion("ab", "eidbaooo")  # True

test = Solution()
test.checkInclusion("ab", "eidboaoo")  # False
