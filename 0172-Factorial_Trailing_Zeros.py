from __future__ import annotations


class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0

        while n:
            n //= 5
            cnt += n

        return cnt
        # print(cnt)


test = Solution()
test.trailingZeroes(3) # 0

test = Solution()
test.trailingZeroes(5) # 1

test = Solution()
test.trailingZeroes(30) # 7
