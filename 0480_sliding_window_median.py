from __future__ import annotations
from typing import List
from heapq import heappop, heappush, heappushpop
from collections import defaultdict


# all heaps in python are minheap. to use minheap as a maxheap u have to make value negative 
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi = [], []
        for i in range(k):
            if len(lo) == len(hi):
                heappush(hi, -heappushpop(lo, -nums[i]))
            else:
                heappush(lo, -heappushpop(hi, nums[i]))
        ans = [float(hi[0])] if k & 1 else [(hi[0] - lo[0]) / 2.0]
        to_remove = defaultdict(int)
        for i in range(k, len(nums)):
            heappush(lo, -heappushpop(hi, nums[i]))
            out_of_window_num = nums[i-k]
            if out_of_window_num > -lo[0]:
                heappush(hi, -heappop(lo))
            to_remove[out_of_window_num] += 1
            while lo and to_remove[-lo[0]]:
                to_remove[-lo[0]] -= 1
                heappop(lo)
            while to_remove[hi[0]]:
                to_remove[hi[0]] -= 1
                heappop(hi)
            if k % 2:
                ans.append(float(hi[0]))
            else:
                ans.append((hi[0] - lo[0]) / 2.0)

        return ans


# test = Solution()
# test.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

test = Solution()
test.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 4)

# test = Solution()
# test.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3)
