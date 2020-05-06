from __future__ import annotations
from timeit import timeit
from functools import partial
from functools import lru_cache
import math

"""
n=3
               DP:  0.000002 seconds
        Recursion:  0.000005 seconds
   Catalan Number:  0.000000 seconds

n=20
               DP:  0.000062 seconds
        Recursion:  0.000055 seconds
   Catalan Number:  0.000004 seconds

n=3
               DP:  0.000002 seconds
        Recursion:  0.000005 seconds
   Catalan Number:  0.000001 seconds
"""


solutions = []

class Solution:
    def numTrees(self, n: int) -> int:
        # G(n): the number of unique BST for a sequence of length n
        G = [0]*(n+1)
        # https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
        G[0] = G[1] = 1

        for i in range(2, n+1): # for a sequence of length n
            for j in range(1, n+1): # root of BST
                G[i] += G[j-1] * G[i-j]

        return G[n]
        # print(G[n])

solutions.append(("DP", Solution().numTrees))


class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache
        def dfs(k: int) -> int:
            if k == 0 or k == 1:
                return 1

            return sum(dfs(i-1) * dfs(k-i) for i in range(1,k+1))

        return dfs(n)
        # print(dfs(n))


solutions.append(("Recursion", Solution().numTrees))


class Solution:
    def numTrees(self, n: int) -> int:
        """
        https://en.wikipedia.org/wiki/Catalan_number
        """
        return int((1/(n+1)) * math.comb(2*n,n))
        # print(int((1/(n+1)) * math.comb(2*n,n)))

solutions.append(("Catalan Number", Solution().numTrees))


for (n, number) in (3, 10**6), (20, 10), (3, 10):
    text = "\nn={}"
    print(text.format(n))
    for name, func in solutions:
        t = timeit(partial(func, n), number=number) / number
        print("  %15s:  %8f seconds" % (name, t))


# test = Solution()
# test.numTrees(3) # 5
