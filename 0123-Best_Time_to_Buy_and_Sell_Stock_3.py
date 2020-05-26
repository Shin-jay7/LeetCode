from __future__ import annotations


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        accProfit, totalProfit, cnt = 0, [], 0

        def calcProfit(prices, minPrice, accProfit, cnt):
            for idx,price in enumerate(prices):
                minPrice = min(minPrice, price)
                profit = price - minPrice
                if profit:
                    if cnt == 0:
                        calcProfit(prices[idx+1:], minPrice, 0, 0)
                        accProfit += profit
                        cnt += 1
                        minPrice = float('inf')
                    else:
                        calcProfit(prices[idx+1:], minPrice, accProfit, 1)
                        accProfit += profit
                        cnt = 0
                        minPrice = float('inf')
                        totalProfit.append(accProfit)
                        accProfit = 0
            totalProfit.append(accProfit)

        calcProfit(prices, minPrice, accProfit, cnt)

        return max(totalProfit) if totalProfit else 0
        # print(max(totalProfit) if totalProfit else 0)


test = Solution()
test.maxProfit([3,3,5,0,0,3,1,4]) # 6

test = Solution()
test.maxProfit([1,2,3,4,5]) # 4

test = Solution()
test.maxProfit([7,6,4,3,1]) # 0

test = Solution()
test.maxProfit([6,1,3,2,4,7]) # 7
