from __future__ import annotations
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, ans = deque(), []
        
        for i, n in enumerate(nums):
            while deq and nums[deq[-1]] < n:
                deq.pop() # 大きい数字がきたら不要な小さい数字のindexトル
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft() # windowから外れたらトル
            ans.append(nums[deq[0]])
            # そのwindow内で最大値のindexが最初に残る

        return ans[k-1:]　
        # windowの最後（k個目）までのmaxが入るので、最初のk-1個分の結果は不要


test = Solution()
test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
# [3,3,5,5,6,7]

test = Solution()
test.maxSlidingWindow([1], 1)
# [1]

test = Solution()
test.maxSlidingWindow([1,-1], 1)
# [1.-1]

test = Solution()
test.maxSlidingWindow([9,11], 2)
# [11]

test = Solution()
test.maxSlidingWindow([4,-2], 2)
# [4]
