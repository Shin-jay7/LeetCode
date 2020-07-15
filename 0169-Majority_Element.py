from __future__ import annotations


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, half = {}, len(nums)//2

        for n in nums:
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1
            if cnt[n] > half:
                return n
                # print(n)
                # return


test = Solution()
test.majorityElement([3,2,3]) # 3

test = Solution()
test.majorityElement([2,2,1,1,1,2,2]) # 2
