from __future__ import annotations
from collections import defaultdict

class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = None
        print(self.trie)

    def search(self, word: str) -> bool:
        nodes = [self.trie]
        for char in word + '#':
            nodes = [kid for node in nodes for kid in
                     ([node[char]] if char in node else
                      filter(None, node.values()) if char == '.' else [])]
            print(nodes)
        return bool(nodes)


test = WordDictionary()
test.addWord('leet')
# test.search('leet')
# test.search('lee')
# test.search('lee.')
test.search('.eet')
