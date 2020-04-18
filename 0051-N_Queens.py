from __future__ import annotations


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(queens: int, posDiff: int, posSum: int) -> None:
            """
            queens is a list of the queen's index in each row on the board
            """
            # print("queens: "+str(queens))
            # print("posDiff: "+str(posDiff))
            # print("posSum: "+str(posSum))
            p = len(queens)
            # print("p: "+str(p))
            if p == n:
                ans.append(queens)
                # print("ans: "+str(ans))
                return
            for q in range(n):
                # print("q: "+str(q))
                # print("p-q: "+str(p-q))
                # print("p+q: "+str(p+q))
                """
                q checks vertical and holizontal lines
                p-q checks top left to botto right diagonal line
                p+q checks top right to bottom left diagonal line
                """
                if q in queens or p-q in posDiff or p+q in posSum:
                    continue
                # print("Trigger another dfs")
                dfs(queens+[q], posDiff+[p-q], posSum+[p+q])

        dfs([],[],[])

        # print([["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans])
        return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in ans]


        # ans = []

        # def dfs(queens, _diff, _sum):
        #     p = len(queens)

        #     if p == n:
        #         queens = ["."*i + "Q" + "."*(n-1-i) for i in queens]
        #         ans.append(queens)
        #         return

        #     for q in range(n):
        #         if q in queens or p-q in _diff or p+q in _sum:
        #             continue
        #         dfs(queens+[q], _diff+[p-q], _sum+[p+q])

        # dfs([],[],[])

        # return ans

test = Solution()
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
