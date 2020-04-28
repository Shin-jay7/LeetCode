from __future__ import annotations


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_ = [int(num) for num in str(int(a) + int(b))]
        carry = 0

        for i in range(len(sum_)-1,-1,-1):
            carry, digit = divmod(sum_[i]+carry, 2)
            sum_[i] = digit

        if carry:
            sum_ = [carry]+sum_

        ans = ""
        for num in sum_:
            ans += str(num)

        return ans
        # print(ans)


test = Solution()
test.addBinary("11", "1") # "100"

test = Solution()
test.addBinary("1", "11") # "100"

test = Solution()
test.addBinary("1010", "1011") # "10101"
