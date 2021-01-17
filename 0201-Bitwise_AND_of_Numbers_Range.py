from __future__ import annotations


https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/593317/Simple-3-line-Java-solution-faster-than-100
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n = n & n-1

        return m & n


test = Solution()
test.rangeBitwiseAnd(5, 7) # 4

test = Solution()
test.rangeBitwiseAnd(0, 1) # 0