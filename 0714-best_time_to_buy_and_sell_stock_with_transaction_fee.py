from __future__ import annotations
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy: max profit when buy a stock
        # sell: max profit when sell a stock
        buy, sell = -prices[0], 0
        for price in prices:
            # print(f'price: {price}')
            buy = max(buy, sell-price)
            # print(f'buy: {buy}')
            sell = max(sell, buy+price-fee)
            # print(f'sell: {sell}')

        return sell


test = Solution()
test.maxProfit([1,3,2,8,4,9], 2) # 8
