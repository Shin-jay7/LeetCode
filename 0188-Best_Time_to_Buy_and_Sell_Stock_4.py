from __future__ import annotations


class Solution:
    def maxProfit(self, n: int, prices: List[int]) -> int:
        """
        dp[i][j][k] represents the best profit we can have at the end of
        the i-th day, 
        with j remaining number of transactions (=buy&sell actions)
        and k holding stocks.

        1. Keep holding the stock
        dp[i][j][k] = dp[i-1][j][k]
        2. Keep not holding the stock
        dp[i][j][0] = dp[i-1][j][0]
        3. Buy when j > 0
        dp[j][j][k] = dp[i-1][j-1][0] - prices[i]
        4. Sell
        dp[i][j][0] = dp[i-1][j][k] + prices[i]

        Combine all the patterns to find the max profit.
        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-1][0] - prices[i])
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][k] + prices[i])
        """

        length, ans = len(prices), 0

        if not prices or n == 0:
            return ans

        if 2*n > length:
            for cur, nex in zip(prices[:-1], prices[1:]):
                ans += max(0, nex - cur)
            return ans

        dp = [[[-float('inf')]*2 for _ in range(n+1)] for _ in range(length)]
        dp[0][0][0], dp[0][1][1] = 0, -prices[0]

        for i in range(1, length):
            for j in range(n+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        ans = max(dp[length-1][j][0] for j in range(n+1))

        return ans





test = Solution()
test.maxProfit(2, [2,4,1]) # 2

test = Solution()
test.maxProfit(2, [3,2,6,5,0,3]) # 7