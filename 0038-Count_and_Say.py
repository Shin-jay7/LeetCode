from __future__ import annotations


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            # print("1")
            # return
            return "1"

        nums = "1"
        for _ in range(n-1):
            pre, cur, ans = nums[0], "", ""
            chunks = []
            for num in nums:
                if num == pre:
                    cur += num
                else:
                    chunks.append(cur)
                    cur = num
                    pre = num
            if cur:
                chunks.append(cur)

            for chunk in chunks:
                ans += str(len(chunk)) + chunk[0]

            nums = ans

        # print(nums)
        return nums



test = Solution()
test.countAndSay(1) # "1"

test = Solution()
test.countAndSay(4) # "1211"
