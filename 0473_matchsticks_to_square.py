from __future__ import annotations
from functools import lru_cache
from typing import List


# https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361
# https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        N = len(matchsticks)
        basket, mod = divmod(sum(matchsticks), 4)
        if mod or max(matchsticks) > basket or N < 4:
            return False

        @lru_cache(None)
        def dfs(mask):
            if mask == 0:
                return 0
            for idx in range(N):
                if mask & (1 << idx):
                    others = dfs(mask ^ (1 << idx))
                    if others >= 0 and others + matchsticks[idx] <= basket:
                        return (others + matchsticks[idx]) % basket
            return -1

        return dfs((1 << N) - 1) == 0
