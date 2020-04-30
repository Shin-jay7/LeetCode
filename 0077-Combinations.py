from __future__ import annotations
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1), k))


test = Solution
test.combine(4, 2)
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
