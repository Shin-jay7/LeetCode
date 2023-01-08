from __future__ import annotations
from functools import cache


# https://leetcode.com/problems/k-inverse-pairs-array/solutions/127746/k-inverse-pairs-array/?orderBy=most_votes
class Solution:
    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if not n:
            return 0
        if not k:
            return 1
        ans, MOD = 0, 10**9+7
        for i in range(min(n-1, k)+1):
            ans = (ans + self.kInversePairs(n-1, k-i)) % MOD
        return ans


# https://leetcode.com/problems/k-inverse-pairs-array/solutions/104824/python-concise-solution/?orderBy=most_votes
# f(0, k) = 0
# f(n, 0) = 1
# f(n, k) = sum(f(n-1, i)) where max(0, k-(n-1)) <= i <= k
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp, MOD = [1] + [0] * k, 10**9+7
        for i in range(2, n+1):
            # Accumulate dp[k] = sum(f(n-1, j)) when 0 <= j <= k
            for j in range(1, k+1):
                dp[j] += dp[j-1]
            # Remove sum(f(n-1, j)) when 0 <= j <= max(0, k-(n-1)) from dp[k]
            for j in range(k, 0, -1):
                dp[j] -= j-i >= 0 and dp[j-i]
        return dp[k] % MOD


# test = Solution()
# test.kInversePairs(0, 1)  # 0

# test = Solution()
# test.kInversePairs(3, 0)  # 1

# test = Solution()
# test.kInversePairs(3, 1)  # 2

# test = Solution()
# test.kInversePairs(2, 1)  # 1
