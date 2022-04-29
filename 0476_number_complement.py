from __future__ import annotations


class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        return int(''.join([str(1 - int(b)) for b in binary]), 2)


# Spread the highest 1 bit onto all the lower bits. Then xor with that.
class Solution:
    def findComplement(self, num: int) -> int:
        mask = num
        mask |= mask >> 1
        mask |= 1 << 1
        mask |= 1 << 2
        mask |= 1 << 4
        mask |= 1 << 8
        mask |= 1 << 16
        return num ^ mask
