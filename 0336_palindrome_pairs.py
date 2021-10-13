from __future__ import annotations
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {w: i for i, w in enumerate(words)}
        ans = []

        for i, w in enumerate(words):
            if w[::-1] in d and d[w[::-1]] != i:
                ans.append([i, d[w[::-1]]])
            if w != '' and w[::-1] == w and '' in d:
                ans.append([i, d['']])
                ans.append([d[''], i])
            for j in range(1, len(w)):
                prefix, suffix = w[:j], w[j:]
                if prefix == prefix[::-1] and suffix[::-1] in d:
                    ans.append([d[suffix[::-1]], i])
                if suffix == suffix[::-1] and prefix[::-1] in d:
                    ans.append([i, d[prefix[::-1]]])

        return ans
