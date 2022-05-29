from __future__ import annotations
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        for i in range(3, len(score)):
            rank[i] = str(i+1)
        place = sorted(score)[::-1]
        ans = []
        for v in score:
            ans.append(rank[place.index(v)])

        return ans


test = Solution()
test.findRelativeRanks([5,4,3,2,1]) 
# ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

test = Solution()
test.findRelativeRanks([10,3,8,9,4])
# ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
