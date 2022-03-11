from __future__ import annotations
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n > 0:
            rows += 1
            n -= rows

        return rows-1


# ith row will be equal to 1 + 2 + 3 + ... + i = i * (i + 1) / 2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right, ans = 1, n, 0
        while left <= right:
            rows = (left+right) // 2
            coins_needed = rows * (rows+1) // 2
            if coins_needed <= n:
                left, ans = rows+1, rows
            else:
                right = rows-1

        return ans


# Solve i * (i + 1) / 2 <= n by math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2*n + .25) - .5)


test = Solution()
test.arrangeCoins(1)  # 1

test = Solution()
test.arrangeCoins(3)  # 2

test = Solution()
test.arrangeCoins(5)  # 2

test = Solution()
test.arrangeCoins(8)  # 3
