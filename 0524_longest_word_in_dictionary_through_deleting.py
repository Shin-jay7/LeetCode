from __future__ import annotations
import itertools
from typing import List
from heapq import heapify, heappop


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word):
            iterative = iter(s)
            return all(char in iterative for char in word)

        dictionary.sort(key=lambda word: (-len(word), word))
        return next(filter(is_subsequence, dictionary), '')


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for word in sorted(dictionary, key=lambda word: (-len(word), word)):
            iterative = iter(s)
            if all(char in iterative for char in word):
                return word
        return ''


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        heap = [(-len(word), word) for word in dictionary]
        heapify(heap)
        while heap:
            word = heappop(heap)[1]
            iterative = iter(s)
            if all(char in iterative for char in word):
                return word
        return ''
