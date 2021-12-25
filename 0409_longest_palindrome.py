from __future__ import annotations
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> str:
        odds = sum(val % 2 for val in Counter(s).values())
        # 奇数の文字が何種類あるか数える
        return len(s) - odds + bool(odds)
        # 奇数の文字の種類を差し引くと、偶数の文字 & 奇数の文字の偶数分が残る
        # bool(odds)はoddsが1以上なら1を返す


test = Solution()
test.longestPalindrome("aabbcccddd")
