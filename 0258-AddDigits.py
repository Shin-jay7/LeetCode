from __future__ import annotations


class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:
            tmp = 0
            for n in list(str(num)):
                tmp += int(n)
            num = tmp

        return num
        # print(num)
        # return


test = Solution()
test.addDigits(38) # 2

test = Solution()
test.addDigits(0) # 0
