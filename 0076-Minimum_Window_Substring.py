from __future__ import annotations
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        dict_t = Counter(t)
        required = len(dict_t)
        l, r, checked, window = 0, 0, 0, {}
        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in dict_t and window[char] == dict_t[char]:
                checked += 1

            while l <= r and checked == required:
                char = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                window[char] -= 1
                if char in dict_t and window[char] < dict_t[char]:
                    checked -= 1
                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
        # print("" if ans[0] == float("inf") else s[ans[1]:ans[2]+1])


test = Solution()
test.minWindow("ADOBECODEBANC", "ABC") # "BANC"
