from __future__ import annotations


class Solution:
    def countAndSay(self, n: int) -> str:
        def cns(nums):
            nums += "#"
            ans = ""
            count = 1
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    count += 1
                else:
                    ans += str(count) + nums[i]
                    count = 1
            return ans

        start = "1"
        for _ in range(n-1):
            start = cns(start)

        return start



test = Solution()
test.countAndSay(1) # "1"

test = Solution()
test.countAndSay(4) # "1211"
