from __future__ import annotations


class Solution:
    def maxProfit(self, n: int, prices: List[int]) -> int:
        length = len(prices)
        if 2*n >= length:
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, length))
            # print(sum(max(0, prices[i]-prices[i-1]) for i in range(1, length)))

        profit = [0]*length
        for _ in range(n):
            max_ = 0
            for i in range(1, length):
                max_ = max(profit[i], max_+prices[i]-prices[i-1])
                profit[i] = max(profit[i-1], max_)
            # print(profit)
        return profit[-1]
        # print(profit[-1])


test = Solution()
test.maxProfit(2, [2,4,1]) # 2

test = Solution()
test.maxProfit(2, [3,2,6,5,0,3]) # 7

test = Solution()
test.maxProfit(2, [3,3,5,0,0,3,1,4]) # 6