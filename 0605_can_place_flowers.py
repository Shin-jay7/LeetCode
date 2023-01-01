from __future__ import annotations
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and\
              (i == 0 or flowerbed[i-1] == 0) and\
              (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                n -= 1
                if n == 0:
                    return True
                flowerbed[i] = 1
        return False


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros, ans = 1, 0  # Initialize zero to 1 and handle prefix easier
        for flower in flowerbed:
            if flower == 0:
                zeros += 1
            else:
                ans += (zeros-1) // 2
                zeros = 0
        return ans + zeros // 2 >= n  # Notice suffix zeros do not need -1


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return sum(
            (len(zeros)-1) // 2 for zeros
            in ''.join(map(str, [0]+flowerbed+[0])).split('1')
        ) >= n
