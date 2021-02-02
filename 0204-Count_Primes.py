from __future__ import annotations


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [1] * n
        primes[0] = primes[1] = 0

        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])

        # i = 2
        # primes[i*i:n:i] = [0] * len(primes[i*i:n:i])

        return sum(primes)
        # print(primes)


test = Solution()
test.countPrimes(30)     