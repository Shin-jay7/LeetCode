from __future__ import annotations
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""

        dict_t = Counter(t)
        required = len(dict_t)

        filtered_s = []
        for idx,char in enumerate(s):
            if char in dict_t:
                filtered_s.append((idx,char))

        l, r, checked, window = 0, 0, 0, {}
        ans = float("inf"), None, None

        while r < len(filtered_s):
            char = filtered_s[r][1]
            window[char] = window.get(char, 0) + 1
            if window[char] == dict_t[char]:
                checked += 1

            while l <= r and checked == required:
                char = filtered_s[l][1]
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end-start+1 < ans[0]:
                    ans = (end-start+1, start, end)
                window[char] -= 1
                if window[char] < dict_t[char]:
                    checked -= 1
                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
        # print("" if ans[0] == float("inf") else s[ans[1]:ans[2]+1])


test = Solution()
test.minWindow("ADOBECODEBANC", "ABC") # "BANC"
