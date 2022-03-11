from __future__ import annotations


class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum, i = 1, 1
        while n >= sum:
            i += 1
            sum += i

        return i-1


test = Solution()
test.arrangeCoins(1)  # 1

test = Solution()
test.arrangeCoins(3)  # 2

test = Solution()
test.arrangeCoins(5)  # 2

test = Solution()
test.arrangeCoins(8)  # 3
