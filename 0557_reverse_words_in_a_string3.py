from __future__ import annotations


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())


# Reverse the order of the words and then reverse the entire string.
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]
