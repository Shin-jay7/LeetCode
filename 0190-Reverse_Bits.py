from __future__ import annotations


class Solution:
    def reverseBits(self, n: int) -> int:
        bits, ans = "", 0
        while n > 0:
            bits = str(n%2) + bits
            n = n//2

        for i, bit in enumerate(bits.zfill(32)):
            ans += int(bit)*(2**i)

        return ans
        # print(bits)
        # print(ans)

test = Solution()
test.reverseBits(43261596) # 964176192

test = Solution()
test.reverseBits(4294967293) # 3221225471