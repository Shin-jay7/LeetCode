from __future__ import annotations
from typing import List


class MagicDictionary:
    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.add((word, len(word)))

    def search(self, searchWord: str) -> bool:
        for word, length in self.words:
            if length != len(searchWord):
                continue
            else:
                cnt = 0
                for i in range(length):
                    if word[i] != searchWord[i]:
                        cnt += 1
                if cnt == 1:
                    return True
        return False
