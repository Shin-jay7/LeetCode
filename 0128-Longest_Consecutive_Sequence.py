from __future__ import annotations


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        cnt, max_ = 1, 0

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                cnt += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_ = max(max_, cnt)
                cnt = 1

        return max(max_, cnt)


test = Solution()
test.longestConsecutive([100, 4, 200, 1, 3, 2])
"""
The longest consecutive elements sequence is [1, 2, 3, 4]
Therefore its length is 4.
"""

test = Solution()
test.longestConsecutive([1, 2, 0, 1])
"""
The longest consecutive elements sequence is [0, 1, 1, 2]
Therefore its length is 3. (What??????????)
"""
