from __future__ import annotations


class Solution:
    def isPowerOfTwo(self, n: int)->bool:
        return n > 0 and not(n & (n-1))
        # Power of 2 means only one bit of n is '1', so use
        # the trick n&(n-1)==0 to judge whether that is the case


test = Solution()
test.isPowerOfTwo(1) # True

test = Solution()
test.isPowerOfTwo(16) # True

test = Solution()
test.isPowerOfTwo(3) # False

test = Solution()
test.isPowerOfTwo(4) # True

test = Solution()
test.isPowerOfTwo(5) # False
