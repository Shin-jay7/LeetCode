from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float('inf'), 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price-minPrice)

        return maxProfit
        # print(maxProfit)


test = Solution()
test.maxProfit([7,1,5,3,6,4]) # 5

test = Solution()
test.maxProfit([7,6,4,3,1]) # 0

test = Solution()
test.maxProfit([]) # 0
