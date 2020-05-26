from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyFirst, sellFirst,  = -float('inf'), 0
        buySecond, sellSecond = -float('inf'), 0

        for price in prices:
            buyFirst = max(buyFirst, -price)
            sellFirst = max(sellFirst, buyFirst+price)
            buySecond = max(buySecond, sellFirst-price)
            sellSecond = max(sellSecond, buySecond+price)

        return max(0, sellSecond)
        # print(max(0, sellSecond))


test = Solution()
test.maxProfit([3,3,5,0,0,3,1,4]) # 6

test = Solution()
test.maxProfit([1,2,3,4,5]) # 4

test = Solution()
test.maxProfit([7,6,4,3,1]) # 0

test = Solution()
test.maxProfit([6,1,3,2,4,7]) # 7

test = Solution()
test.maxProfit([]) # 0
