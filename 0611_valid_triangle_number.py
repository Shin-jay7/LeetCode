from __future__ import annotations
from typing import List


# https://leetcode.com/problems/valid-triangle-number/solutions/1339340/c-java-python-two-pointers-picture-explain-clean-concise-o-n-2/?orderBy=most_votes
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n, ans = len(nums), 0
        for k in range(2, n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ans += j-i
                    j -= 1
                else:
                    i += 1
        return ans


test = Solution()
test.triangleNumber([2,2,3,4])
