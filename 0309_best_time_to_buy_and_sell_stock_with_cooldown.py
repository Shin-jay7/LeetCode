from __future__ import annotations
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        diff = [prices[i+1] - prices[i] for i in range(n-1)]
        dp, dp_max = [0]*(n+1), [0]*(n+1)
        for i in range(n-1):
            dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
            dp_max[i] = max(dp_max[i-1], dp[i])

        return dp_max[-3]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sold is the maximum profit I can have while being free to buy.
        hold is the maximum profit I can have while having stock.
        cool is the maximum profit I can have while cooling down.
        """
        sold, hold, cool = 0, float('-inf'), float('-inf')
        for p in prices:
            sold, hold, cool = max(sold, cool), max(hold, sold-p), hold+p

        return max(sold, cool)
