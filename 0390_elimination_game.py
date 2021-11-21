from __future__ import annotations


class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = range(1, n+1)
        while len(arr) > 1:
            arr = arr[1::2][::-1]
        return arr[0]


class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        if n & 1:
            n -= 1
        return n + 2 - 2*self.lastRemaining(n//2)
