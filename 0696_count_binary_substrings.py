from __future__ import annotations


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # count the number of 1 or 0 grouped consecutively.
        # For example "0110001111" will be [1, 2, 3, 4].
        # Then for any possible substrings with 1 and 0 grouped consecutively,
        # the number of valid substring will be the minimum number of 0 and 1.
        # For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")
        curr, prev, cnt = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                cnt += min(curr, prev)
                prev, curr = curr, 1
        return cnt + min(curr, prev)
