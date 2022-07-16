from __future__ import annotations
from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        cache = {}

        def helper(perm):
            digits = len(perm)
            if digits == 1:
                return 1
            if perm in cache:
                return cache[perm]
            cnt = 0
            for i in range(digits):
                if perm[i] % digits == 0 or digits % perm[i] == 0:
                    cnt += helper(perm[:i] + perm[i+1:])
            cache[perm] = cnt
            return cnt

        return helper(tuple(range(1, n+1)))


class Solution:
    def countArrangement(self, n: int) -> int:
        # total number of bitset states possible
        bitset_total = 2**n
        dp = [[0 for _ in range(bitset_total)]
              for _ in range(n+1)]
        # all other valid states lead to this base case so mark this as 1
        dp[0][0] = 1
        # iterate over all positions
        for i in range(1, n+1):
            # iterate over all subsets
            for bm in range(bitset_total):
                # iterate over all numbers
                for num in range(n):
                    # if number is not visited and satisfies condition in question
                    #  & （各桁が両方とも1なら1になる）
                    # 1 << x (1を左にxシフトさせて右をゼロで埋める)
                    #  ^ （XOR: 各桁の片方が1なら1になる）
                    if ((bm & (1 << num)) and
                        (((num+1) % i == 0) or
                         (i % (num+1) == 0))):
                        dp[i][bm] += dp[i-1][bm ^ (1 << num)]
        return dp[-1][-1]


# bm is binary mask for visited numbers.
# i is current place we want to fill. 
# Idea is to start from the end, and fill places in opposite direction,
# because for big numbers we potentially have less candidates.
# how dfs(bm, pl) will work:
# If we reached place 0 and procces was not interrupted so far,
# it means that we find beautiful arrangement.
# For each number 1, 2, ..., n we try to put this number on place pl:
# and we need to check two conditions: first, that this place is still empty,
# using bitmask and secondly that one of the two properties for beutiful arrangement
# holds. In this case we add dfs(bm^1<<i, pl - 1) to final answer.
# Finally, we run dfs(0, n): from the last place and with empty bit-mask.
class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(bm, i):
            if i == 0:
                return 1

            cnt = 0
            for num in range(n):
                if not bm & 1 << num\
                   and ((num+1) % i == 0 or i % (num+1) == 0):
                    cnt += dfs(bm ^ 1 << num, i-1)
            return cnt

        return dfs(0, n)


# nums is the set of still available numbers.
# Note that my i goes downwards, from n to 1. Because position i = 1
# can hold any number, so I don't even have to check whether the last
# remaining number fits there. Also, position i = 2 happily holds
# every second number and i = 3 happily holds every third number,
# so filling the lowest positions last has a relatively high chance of success.
class Solution:
    def countArrangement(self, n: int) -> int:
        def count(i, nums):
            if i == 1:
                return 1
            return sum(count(i-1, nums-{num})
                       for num in nums
                       if num % i == 0 or i % num == 0)
        return count(n, set(range(1, n+1)))
