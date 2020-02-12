from __future__ import annotations


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x*(-1)
            ans = int(str(x)[::-1])*(-1)
        else:
            ans = int(str(x)[::-1])

        if ans >= 2147483648 or ans < -2147483648:
            return 0
        else:
            return ans


test = Solution()
test.reverse(1534236469) # 0

test = Solution()
test.reverse(123) # 321

test = Solution()
test.reverse(-123) # -321

test = Solution()
test.reverse(120) # 21
