from __future__ import annotations
from typing import List


# Start with the numbers sorted, e.g., 1 2 3 4 5 6 7 8 9 10. 
# Then we only have difference 1, many times. We can create the largest
# possible difference by making the smallest and largest number neighbors.
# In the example, let's bring 10 next to 1. If we do this by reversing 
# the whole subarray from 2 to 10, then no other neighborships in 2 to 10
# are affected: 1 10 9 8 7 6 5 4 3 2. To create the next larger possible
# difference, we can bring 2 next to 10 by reversing the subarray from 9 to 2:
# 1 10 2 3 4 5 6 7 8 9. And so on, reversing shorter and shorter suffixes.
# Just create as many differences as requested.
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n+1))
        for i in range(1, k):
            ans[i:] = ans[:i-1:-1]
        return ans


# Continue flips from the end
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        flag, diff = 1, k
        ans = list(range(1, n-k+1))
        for i in range(k):
            ans.append(ans[-1] + flag * diff)
            flag *= -1
            diff -= 1
        return ans
