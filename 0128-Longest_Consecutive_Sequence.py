from __future__ import annotations


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set() takes O(n) time
        nums, max_ = set(nums), 0

        for n in nums:
            if n-1 not in nums:
                consec = n+1
                while consec in nums:
                    consec += 1
                max_ = max(max_, consec-n)

        return max_


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
