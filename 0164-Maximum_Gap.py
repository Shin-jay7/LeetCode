from __future__ import annotations


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2 or min(nums) == max(nums): return 0
        sorted(nums)
        max_ = 0

        for i in range(n-1):
            max_ = max(max_, nums[i+1]-nums[i])

        return max_
        # print(max_)
        # return

# Approach 3: Buckets and The Pigeonhole Principle
# https://leetcode.com/problems/maximum-gap/solution/
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        a, b = min(nums), max(nums)
        if a == b: return 0
        size = (b-a)//(n-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]

        for num in nums:
            b = bucket[(num-a)//size]
            b[0] = num if b[0] is None else min(b[0], num)
            b[1] = num if b[1] is None else max(b[1], num)

        bucket = [b for b in bucket if b[0] is not None]

        return max(bucket[i][0]-bucket[i-1][1] for i in range(1,len(bucket)))


test = Solution()
test.maximumGap([3,6,9,1]) # 3

# test = Solution()
# test.maximumGap()
