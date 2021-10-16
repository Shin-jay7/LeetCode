from __future__ import annotations
from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=lambda x: [x[0], -x[1]])
        dp = [10**10] * (len(envelopes)+1)
        for env in envelopes:
            dp[bisect_left(dp, env[1])] = env[1]
            # print(dp)

        return dp.index(10**10)
        # print(dp.index(10**10))


test = Solution()
test.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) # 3

test = Solution()
test.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]) # 4

test = Solution()
test.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]) # 5
