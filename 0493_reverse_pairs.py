from __future__ import annotations
from typing import List
from sortedcontainers import SortedList


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        lst = SortedList()
        cnt = 0
        for i, n in enumerate(nums):
            idx = lst.bisect_right(-2 * n - 1)
            lst.add(-n)
            cnt += idx
        return cnt


class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.sums = [0] * self.n

    def update(self, i, delta):
        while i < self.n:
            self.sums[i] += delta
            i += i & -i # i & -i: 最も下位に1が立っているビットのみ残した値を抽出する

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= i & -i
        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        bit = BIT(n)
        nums = (
            [(num, 1, idx) for idx, num in enumerate(nums)] +
            [(2 * num, 2, idx) for idx, num in enumerate(nums)]
        )
        ans = 0
        for _, cnt, idx in sorted(nums):
            if cnt == 1:
                ans += bit.query(n - idx - 1)
            else:
                bit.update(n - idx, 1)

        return ans


test = Solution()
test.reversePairs([1,3,2,3,1]) # 2

