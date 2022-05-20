from __future__ import annotations
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        return [
            word for word in words
            if any(set(word.lower()) <= row for row in rows)]
