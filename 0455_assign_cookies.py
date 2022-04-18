from __future__ import annotations
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child, cookie = 0, 0
        g_len, s_len = len(g), len(s)
        g.sort()
        s.sort()
        while child < g_len and cookie < s_len and g[child] <= s[-1]:
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1

        return child
