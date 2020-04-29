from __future__ import annotations


class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a+b

        return a

test = Solution()
test.climbStairs(1) # 1

test = Solution()
test.climbStairs(2) # 2

test = Solution()
test.climbStairs(3) # 3
