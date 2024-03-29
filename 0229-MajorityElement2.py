from __future__ import annotations
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt, ans = Counter(), []

        for n in nums:
            cnt[n] += 1

        for n in cnt:
            if cnt[n] > len(nums)//3:
                ans.append(n)

        return ans
        # print(ans)


test = Solution()
test.majorityElement([3,2,3]) # 3

test = Solution()
test.majorityElement([1]) # 1

test = Solution()
test.majorityElement([1,2]) # 1,2
