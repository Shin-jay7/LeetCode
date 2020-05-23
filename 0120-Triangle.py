from __future__ import annotations


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return
        dp = triangle[-1]

        for i in range(len(triangle)-2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]
        # print(dp[0])


test = Solution()
test.minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]]) # 11

test = Solution()
test.minimumTotal([[-1], [3,2], [-3,1,-1]]) # -1
