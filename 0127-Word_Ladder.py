from __future__ import annotations
from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str,\
                     endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        allCombo, n = defaultdict(list), len(beginWord)

        for word in wordList:
            for idx in range(n):
                allCombo[word[:idx] + "*" + word[idx+1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            nextWord, level = queue.popleft()
            for idx in range(n):
                pattern = nextWord[:idx] + "*" + nextWord[idx+1:]
                for word in allCombo[pattern]:
                    if word == endWord:
                        # print(level+1)
                        # return
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))

        return 0


test = Solution()
test.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5

test = Solution()
test.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) # 0

test = Solution()
test.ladderLength("kiss", "tusk",\
 ["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"])
# 5
