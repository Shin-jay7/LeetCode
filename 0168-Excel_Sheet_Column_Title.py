from __future__ import annotations


class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""

        while n:
            n, m = divmod(n, 26)
            ans = alphabet[m-1] + ans
            if m == 0: n -= 1

        return ans
        # print(ans)


test = Solution()
test.convertToTitle(1) # "A"

test = Solution()
test.convertToTitle(28) # "AB"

test = Solution()
test.convertToTitle(701) # "ZY"

test = Solution()
test.convertToTitle(27) # "AA"

test = Solution()
test.convertToTitle(52) # "AZ"
