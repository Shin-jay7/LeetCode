from __future__ import annotations


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            if n&1:
                cnt += 1
            n >>= 1

        return cnt
        # print(cnt)


test = Solution()
test.hammingWeight(11) # 3

test = Solution()
test.hammingWeight(128) # 1