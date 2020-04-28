from __future__ import annotations


# https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1

        ans = x//2
        while ans*ans > x:
            ans = int((ans + x/ans) / 2)

        return ans
        # print(ans)

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

