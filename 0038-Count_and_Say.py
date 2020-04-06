from __future__ import annotations
import itertools


class Solution:
    def countAndSay(self, n: int) -> str:
        nums = "1"
        for _ in range(n-1):
            temp = ""
            for num, group in itertools.groupby(nums):
                count = len(list(group))
                temp += str(count) + num
            nums = temp

        return nums


test = Solution()
test.countAndSay(1) # "1"

test = Solution()
test.countAndSay(4) # "1211"
