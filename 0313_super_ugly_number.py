from __future__ import annotations
from typing import List
from heapq import heappop, heappush, merge


# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: List[int]):
#         size = len(primes)
#         ugly, dp, index, ugly_nums = 1, [1], [0]*size, [1]*size
#         for i in range(1, n):
#             for j in range(0, size):
#                 if ugly_nums[j] == ugly:
#                     ugly_nums[j] = dp[index[j]] * primes[j]
#                     index[j] += 1
#             ugly = min(ugly_nums)
#             dp.append(ugly)

#         return dp[-1]


# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: List[int]):
#         cnt, h = 1, []
#         nums = [0] * (n+1)
#         nums[0] = 1

#         for prime in primes:
#             heappush(h, (prime, prime, 0))

#         while cnt < n:
#             entry = heappop(h)
#             num, prime, index = entry[0], entry[1], entry[2]
#             if num != nums[cnt-1]:
#                 nums[cnt] = num
#                 cnt += 1
#             heappush(h, (prime*nums[index+1], prime, index+1))

#         return nums[n-1]


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]):
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                # print(ugly, f'--calling from {prime}')
                yield ugly * prime

        merged = merge(*map(gen, primes))
        # print(next(merged))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)

        return uglies[-1]
        # print(uglies[-1])


test = Solution()
test.nthSuperUglyNumber(12, [2,7,13,19]) #32
