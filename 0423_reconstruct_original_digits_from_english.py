from __future__ import annotations
from collections import Counter


# https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/91210/Fun-fact
class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        digits = ["zero", "one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]
        freq = [0] * 10
        for char, i in ("z", 0), ("w", 2), ("u", 4), ("x", 6), ("g", 8),\
                       ("s", 7), ("f", 5), ("o", 1), ("h", 3), ("i", 9):
            freq[i] += counter[char]
            counter -= Counter(digits[i] * counter[char])

        return "".join(str(idx)*cnt for idx, cnt in enumerate(freq))
