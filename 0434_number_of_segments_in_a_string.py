from __future__ import annotations


class Solution:
    def countSegments(self, s: str) -> int:
        flag, ans = 0, 0
        for char in s:
            if char == " ":
                if flag:
                    ans += 1
                flag = 0
            else:
                flag = 1

        return ans+1 if flag == 1 else ans


class Solution:
    def countSegments(self, s: str) -> int:
        length, cnt = len(s.strip()), 0
        if not length:
            return 0
        for i in range(length-1):
            if s[i] == " " and s[i+1] != " ":
                cnt += 1
        return cnt + 1
        