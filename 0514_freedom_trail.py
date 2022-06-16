from __future__ import annotations
from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        idxes = defaultdict(list)
        n = len(ring)
        dp = [0] * n
        pre = key[0]

        for i, c in enumerate(ring):
            idxes[c].append(i)
        for i in idxes[key[0]]:
            dp[i] = min(i, n-i) + 1
        for c in key[1:]:
            for i in idxes[c]:
                dp[i] = min(
                        dp[j] + min(abs(i-j), n - abs(i-j)) for j in idxes[pre]
                      ) + 1
            pre = c

        return min(dp[i] for i in idxes[key[-1]])
