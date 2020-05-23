from __future__ import annotations


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)
        dp = [[0]*(_+1) for _ in range(length)]

        for i in range(length):
            for j in range(i+1):
                if i > 1 and 0 < j < i:
                    dp[i][j] =\
                    min(dp[i-1][j-1], dp[i-1][j])
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][j]
                elif i > 0 and j == i:
                    dp[i][j] = dp[i-1][j-1]
                dp[i][j] += triangle[i][j]

        return min(dp[-1])
        # print(min(dp[-1]))


test = Solution()
test.minimumTotal([[2], [3,4], [6,5,7], [4,1,8,3]]) # 11

test = Solution()
test.minimumTotal([[-1], [3,2], [-3,1,-1]]) # -1
