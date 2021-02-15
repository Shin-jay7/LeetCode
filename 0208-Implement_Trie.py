from __future__ import annotations


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
            print(self.trie)
        t['#'] = '#'
        print(self.trie)

    def search(self, word: str) -> bool:
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for p in prefix:
            if p not in t:
                return False
            t = t[p]
        return True


class Trie:
    def __init__(self):
        self.setWord = set()
        self.setPrefix = set()

    def insert(self, word: str) -> None:
        self.setWord.add(word)
        for i in range(len(word)):
            self.setPrefix.add(word[:i+1])

    def search(self, word: str) -> bool:
        if word in self.setWord:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.setPrefix:
            return True
        return False
