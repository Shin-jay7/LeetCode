from __future__ import annotations
from typing import List
from xml.dom import WrongDocumentErr


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)

        def search(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    d.add(word)
                    return True
                if prefix in d and search(suffix):
                    d.add(suffix)
                    d.add(word)
                    return True
            return False

        return [word for word in words if search(word)]
