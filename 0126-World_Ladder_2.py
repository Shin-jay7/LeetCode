from __future__ import annotations
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str,\
                    wordList: List[str]) -> List[List[str]]:
        tree, words, n = defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        beginQ, endQ, matchedQ = {beginWord}, {endWord}, set()
        found, reverseKeyValue = False, False

        while beginQ and not found:
            words -= set(beginQ)
            for bWord in beginQ:
                for idx in range(n):
                    first, second = bWord[:idx], bWord[idx+1:]
                    for char in 'qwertyuiopasdfghjklzxcvbnm':
                        word = first + char + second
                        if word in words:
                            if word in endQ:
                                found = True
                            else:
                                matchedQ.add(word)
                            tree[word].add(bWord) if reverseKeyValue\
                                                  else tree[bWord].add(word)
                beginQ, matchedQ = matchedQ, set()

                """
                BFS't time complexity is O(b^d) where b is branch factor
                and d is depth. So if we go with a bi-directional way,
                expanding from both being word and end word, and choosing
                the queue ('begin' queue or 'end' queue) with smaller size
                in each expansion, the branch factor will be greatly reduced.
                """
                if len(beginQ) > len(endQ):
                    beginQ, endQ = endQ, beginQ
                    reverseKeyValue = not reverseKeyValue

        def bt(x):
            return [[x]] if x == endWord\
                   else [[x]+rest for y in tree[x] for rest in bt(y)]

        return bt(beginWord)
        # print(bt(beginWord))


test = Solution()
test.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
"""
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
"""

test = Solution()
test.findLadders("hit", "cog",  ["hot","dot","dog","lot","log"])
"""
[]
"""
