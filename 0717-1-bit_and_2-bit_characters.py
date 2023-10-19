from __future__ import annotations
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                if i == len(bits)-1:
                    return True
                i += 1
            else:
                i += 2
        return False


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i < n-1:
            i += bits[i] + 1
        return n-i == 1
