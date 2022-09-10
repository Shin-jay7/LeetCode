from __future__ import annotations


# dp[i]the number of all possible attendance (without 'A') records with length i :
# end with "P": dp[i-1]
# end with "PL": dp[i-2]
# end with "PLL": dp[i-3]
# end with "LLL": is not allowed
# so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 3
        MOD = 1000000007
        dp = [1, 2, 4]
        for i in range(3, n+1):
            dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % MOD)
        ans = dp[n]
        for i in range(n):
            # you can split the array in all possible places and then insert A.
            # For each dp[i], there are dp[i] * dp[n-1-i] combinations to get a
            # result with length n. The result looks like dp[i] +'A'+ dp[n-1-i].
            ans = (ans + dp[i] * dp[n-1-i]) % MOD
        return ans
