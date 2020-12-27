from __future__ import annotations


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans<<1) + (n&1)
            n >>= 1

        return ans
        # print(ans)


class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(16):
            ans |= ((n>>i)&1)<<(31-i) | ((n>>(31-i))&1)<<i

        return ans
        # print(ans)


test = Solution()
test.reverseBits(43261596) # 964176192

test = Solution()
test.reverseBits(4294967293) # 3221225471