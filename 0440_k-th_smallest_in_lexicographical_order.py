from __future__ import annotations


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1
        k -= 1

        while k > 0:
            remainder = 0
            min_max = [ans, ans+1]
            while min_max[0] <= n:
                remainder += (min(n+1, min_max[1]) - min_max[0])
                min_max = [10*min_max[0], 10*min_max[1]]
            if k >= remainder:
                ans += 1
                k -= remainder
            else:
                ans *= 10
                k -= 1

        return ans
