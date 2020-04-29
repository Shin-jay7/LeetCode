from __future__ import annotations
from functools import lru_cache


# https://stackoverflow.com/questions/49883177/how-does-lru-cache-from-functools-work
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)

        def dp(i,j):
            if i < 0 or j < 0:
                return max(i,j)+1
            if word1[i] == word2[j]:
                return dp(i-1, j-1)
            else:
                return min(dp(i-1,j), dp(i-1,j-1), dp(i,j-1)) + 1

        return dp(len(word1)-1, len(word2)-1)
        # print(dp(len(word1)-1, len(word2)-1))


test = Solution()
test.minDistance("horse", "ros") # 3

test = Solution()
test.minDistance("intention", "execution") # 5
