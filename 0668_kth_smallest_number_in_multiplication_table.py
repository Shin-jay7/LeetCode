from __future__ import annotations


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def larger_than_k(target: int) -> bool:
            cnt = 0
            for i in range(1, m+1):
                # Count nums equal or smaller than target in each row.
                # Notice nums in each row: i, 2*i, 3*i, ..., n*i
                cnt += min(target//i, n)
            return cnt >= k

        left, right = 1, m*n
        while left < right:
            mid = (left+right) // 2
            if larger_than_k(mid):
                right = mid
            else:
                left = mid+1
        return left


test = Solution()
test.findKthNumber(3, 3, 5)  # 3
