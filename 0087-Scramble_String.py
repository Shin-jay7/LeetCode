from __future__ import annotations


class Solution:
    def __init__(self):
        self.dic = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]

        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.dic[(s1, s2)] = False
            return False

        if len(s1) < 4 or s1 == s2:
            self.dic[(s1, s2)] = True
            return True

        f = self.isScramble
        for i in range(1, len(s1)):
            if f(s1[:i], s2[:i])  and f(s1[i:], s2[i:]) or\
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                self.dic[(s1, s2)] = True
                return True

        self.dic[(s1, s2)] = False

        return False


test = Solution()
test.isScramble("great", "rgeat") # True

test = Solution()
test.isScramble("abcde", "caebd") # False
