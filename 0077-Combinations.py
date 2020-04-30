from __future__ import annotations
from itertools import combinations
from timeit import timeit
from functools import partial

solutions = []


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1), k))

solutions.append(("Library", Solution().combine))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre+[i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]

solutions.append(("Recursive", Solution().combine))


for (n, k, number) in (2, 2, 10**6), (1000, 2, 10**1), (20, 20, 10):
    print("\nn=%d k=%d" % (n, k))
    for name, func in solutions:
        t = timeit(partial(func, n, k), number=number) / number
        print("  %7s:  %.8f seconds" % (name, t))


# test = Solution()
# test.combine(4, 2)
"""
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
