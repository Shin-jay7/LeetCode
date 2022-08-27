from __future__ import annotations


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        while s:
            size = len(s)
            if size >= 2*k:
                ans += s[:k][::-1] + s[k:2*k]
            elif size >= k:
                ans += s[:k][::-1] + s[k:]
            else:
                ans += s[::-1]
            s = s[2*k:]

        # print(ans)
        return ans


test = Solution()
test.reverseStr("abcdefg", 2) # "bacdfeg"

test = Solution()
test.reverseStr("abcd", 2) # "bacd"
