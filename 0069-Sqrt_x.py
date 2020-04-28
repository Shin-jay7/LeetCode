from __future__ import annotations


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        lo, hi = 1, x

        while lo < hi:
            mid = lo + (hi-lo+1)//2
            if mid <= x//mid:
                lo = mid
            else:
                hi = mid-1

        return lo
        # print(lo)

test = Solution()
test.mySqrt(1) # 1

test = Solution()
test.mySqrt(4) # 2

test = Solution()
test.mySqrt(8) # 2

test = Solution()
test.mySqrt(7) # 2

test = Solution()
test.mySqrt(9) # 3

test = Solution()
test.mySqrt(2147395599) #

