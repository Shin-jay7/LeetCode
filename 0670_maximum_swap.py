from __future__ import annotations


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(n) for n in str(num)]
        max_idx = len(num) - 1
        x, y = 0, 0
        for i in range(len(num)-1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                x, y = i, max_idx
        num[x], num[y] = num[y], num[x]
        return int(''.join([str(n) for n in num]))
