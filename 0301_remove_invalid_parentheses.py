from __future__ import annotations
from typing import List, bool


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        levels = {s}

        while True:
            ans = []
            for level in levels:
                if self.isValid(level):
                    ans.append(level)
            if ans:
                return ans
            candidates = set()
            for level in levels:
                for i in range(len(level)):
                    candidates.add(level[:i] + level[i + 1:])
            levels = candidates

    def isValid(self, s) -> bool:
        cnt = 0

        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False

        return cnt == 0
