from __future__ import annotations
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(word1, word2):
            iterative = iter(word2)
            return all(char in iterative for char in word1)

        for word1 in sorted(strs, key=len, reverse=True):
            if sum(is_subsequence(word1, word2) for word2 in strs) == 1:
                # Please notice uncommon subsequence returns False.
                # The above returns 1 only when word1 matches with itself,
                # so all other candidate words are uncommon subsequences.
                return len(word1)
        return -1
