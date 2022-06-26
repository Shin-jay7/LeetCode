from __future__ import annotations
from typing import List


# https://qiita.com/drken/items/a5e6fe22863b7992efdb
# dp[i][j] : the number of combinations to make up amount j 
# by using the first i types of coins
# 1) not using the ith coin, only using the first i-1 coins to make up amount j, 
#    then we have dp[i-1][j] ways.
# 2) using the ith coin, since we can use unlimited same coin, we need to know 
#    how many ways to make up amount j - coins[i-1] by using first i coins(including ith),
#    which is dp[i][j-coins[i-1]]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1)] * (len(coins)+1)
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(coins)][amount]


# Now we can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]], 
# then we can optimize the space by only using one-dimension array.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]

        return dp[amount]
