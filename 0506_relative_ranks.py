from __future__ import annotations
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        place = sorted(score)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"]\
            + list(map(str, range(4, len(score)+1)))
        return list(map(dict(zip(place, rank)).get, score))


test = Solution()
test.findRelativeRanks([5,4,3,2,1]) 
# ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

test = Solution()
test.findRelativeRanks([10,3,8,9,4])
# ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
