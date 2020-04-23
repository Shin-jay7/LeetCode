from __future__ import annotations
from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return "".join(map(str, (list(permutations(range(1,n+1)))[k-1])))
        # print("".join(map(str, (list(permutations(range(1,n+1)))[k-1]))))


test = Solution()
test.getPermutation(3,3) # "213"

test = Solution()
test.getPermutation(4,9) # "2314"
