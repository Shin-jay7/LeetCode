from __future__ import annotations


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        ans = [1,1]+[0]*(n-1)

        for i in range(2,n+1):
            ans[i] = ans[i-1]+ans[i-2]

        return ans[-1]
        # print(ans[-1])

test = Solution()
test.climbStairs(1) # 1

test = Solution()
test.climbStairs(2) # 2

test = Solution()
test.climbStairs(3) # 3
