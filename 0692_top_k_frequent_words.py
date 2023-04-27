from __future__ import annotations
from typing import List
from collections import Counter
from heapq import nsmallest


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict(Counter(words))
        return sorted(d, key=lambda word: (-d[word], word))[:k]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return nsmallest(k, counter, key=lambda word: (-counter[word], word))


test = Solution()
test.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
# ["i", "love"]

test = Solution()
test.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3)
# ["i", "love", "coding"]
