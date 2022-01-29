from __future__ import annotations
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32)[::-1]:
            ans <<= 1
            prefixes = {num >> i for num in nums}
            ans += any(ans ^ 1 ^ p in prefixes for p in prefixes)
        return ans


test = Solution()
test.findMaximumXOR([3,10,5,25,2,8]) # 28

test = Solution()
test.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]) # 127
