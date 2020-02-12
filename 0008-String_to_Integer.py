from __future__ import annotations
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        ans = 0
        matchObj = re.match(r'\s*(-?\d+|\+?\d+)', str)
        if matchObj == None:
            return 0
        else:
            ans = int(matchObj.group(1))

        if ans >= 2147483648:
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        else:
            return ans


test = Solution()
test.myAtoi("++1") # 1

test = Solution()
test.myAtoi("+-2") # -2

test = Solution()
test.myAtoi("+1") # 1

test = Solution()
test.myAtoi("42") # 42

test = Solution()
test.myAtoi("     -42") # -42

test = Solution()
test.myAtoi("4193 with words") # 4193

test = Solution()
test.myAtoi("words and 987") # 0

test = Solution()
test.myAtoi("-91283472332") # -2147483648 <- INT_MIN (-2**31)
