from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0

        profits, curMaxProfit, curMinPrice = [], 0, float('inf')

        # Calculate max profit by the ith day
        for price in prices:
            curMinPrice = min(curMinPrice, price)
            curMaxProfit = max(curMaxProfit, price-curMinPrice)
            profits.append(curMaxProfit)

        total, curMaxProfit, curMaxPrice = 0, 0, 0

        # Calculate max profit after the ith day
        for i in range(len(prices)-1, -1, -1):
            curMaxPrice = max(curMaxPrice, prices[i])
            curMaxProfit = max(curMaxProfit, curMaxPrice-prices[i])
            total = max(total, curMaxProfit+profits[i])

        return total
        # print(total)


test = Solution()
test.maxProfit([3,3,5,0,0,3,1,4]) # 6

test = Solution()
test.maxProfit([1,2,3,4,5]) # 4

test = Solution()
test.maxProfit([7,6,4,3,1]) # 0

test = Solution()
test.maxProfit([6,1,3,2,4,7]) # 7
