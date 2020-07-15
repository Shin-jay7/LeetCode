from __future__ import annotations


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, candidate = 0, None

        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if num == candidate else -1

        return candidate


test = Solution()
test.majorityElement([3,2,3]) # 3

test = Solution()
test.majorityElement([2,2,1,1,1,2,2]) # 2
