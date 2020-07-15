from __future__ import annotations

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        return max(cnts.keys(), key=cnts.get)


test = Solution()
test.majorityElement([3,2,3]) # 3

test = Solution()
test.majorityElement([2,2,1,1,1,2,2]) # 2
