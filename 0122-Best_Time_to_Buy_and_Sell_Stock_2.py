from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            profit += max(prices[i]-prices[i-1], 0)

        return profit


test = Solution()
test.maxProfit([7,1,5,3,6,4]) # 7

test = Solution()
test.maxProfit([1,2,3,4,5]) # 4

test = Solution()
test.maxProfit([6,1,3,2,4,7]) # 7
