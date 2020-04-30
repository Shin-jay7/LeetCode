from __future__ import annotations
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        missing = len(t)
        start, end, i = 0, 0, 0

        for j,char in enumerate(s,1):
            """
            Suppose we change to enumerate from 0, then we want to return
            s[start, end+1]. If there's no matching substring (e.g. s = 'a',
            t = 'ab'), 'start' and 'end' will not be changed and we are
            returning s[0, 1] (i.e. 'a' instead of ''). This is incorrect.
            An alternative way:
            1) change end = 0 to end = -1,
            2) enumerate from 0
            3) change if end == 0 to end == -1
            4) return s[start: end+1]
            """
            if dict_t[char] > 0:
                missing -= 1
            dict_t[char] -= 1

            if not missing:
                while i < j and dict_t[s[i]] < 0:
                    dict_t[s[i]] += 1
                    i += 1
                dict_t[s[i]] += 1
                missing += 1

                if end == 0 or j-i < end-start:
                    start, end = i, j
                i += 1

        return s[start:end]
        # print(s[start:end])



test = Solution()
test.minWindow("ADOBECODEBANC", "ABC") # "BANC"
