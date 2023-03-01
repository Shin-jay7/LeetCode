from __future__ import annotations
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for root in dictionary:
            sentence = [root if word.startswith(root) else word
                        for word in sentence]
        return " ".join(sentence)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        _trie = {}
        for root in dictionary:
            trie = _trie
            for char in root:
                if char not in trie:
                    trie[char] = {}
                trie = trie[char]
            trie['#'] = '#'

        def replace(word):
            trie = _trie
            for idx, char in enumerate(word):
                if char not in trie:
                    break
                trie = trie[char]
                if '#' in trie:
                    return word[:idx+1]
            return word

        return " ".join(map(replace, sentence.split()))


test = Solution()
test.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
# "the cat was rat by the bat"

test = Solution()
test.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs")
# "a a b c"
