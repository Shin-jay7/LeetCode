from __future__ import annotations


class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0

        def dfs(queens: List[int], posDiff: List[int],\
                posSum: List[int]) -> None:
            p = len(queens)
            if p == n:
                self.cnt += 1
                return
            for q in range(n):
                if q in queens or p-q in posDiff or p+q in posSum:
                    continue
                else:
                    dfs(queens+[q], posDiff+[p-q], posSum+[p+q])

        dfs([],[],[])

        # print(self.cnt)
        return self.cnt




test = Solution()
test.totalNQueens(4) ## 2
