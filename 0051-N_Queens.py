from __future__ import annotations


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(queens: int, posDiff: int, posSum: int) -> None:
            p = len(queens)
            if p == n:
                ans.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in posDiff and p+q not in posSum:
                    dfs(queens+[q], posDiff+[p-q], posSum+[p+q])

        dfs([],[],[])

        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]


test.Solution()
test.solveNQueens(4)
"""
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]
"""
