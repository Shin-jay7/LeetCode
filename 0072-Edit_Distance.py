from __future__ import annotations


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Why does this cause the wrong answer?
        # dp = [[0]*(n+1)]*(m+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        """
        Define the state dp[i][j] is edit distance from
        word1's first i letters to word2's first j letters.
        To convert a string to an empty string, the mininum
        number of operations (deletions) is just the length of
        the string. So we have dp[i][0] = i and dp[0][j] = j.
        """
        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # dp[i-1][j-1] + 1 (replace)
                    # dp[i-1][j] + 1 (remove)
                    # dp[i][j-1] + 1 (insert)
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[-1][-1]
        # print(dp[-1][-1])
        # print(dp)



# test = Solution()
# test.minDistance("horse", "ros") # 3

test = Solution()
test.minDistance("intention", "execution") # 5
