from __future__ import annotations


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        def move(row, col, moves):
            cnt = 0
            if moves < 0:
                return 0
            if not (0 <= row < m and 0 <= col < n):
                return 1

            for row_move, col_move in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                cnt += move(row+row_move, col+col_move, moves-1)

            return cnt

        return move(startRow, startColumn, maxMove) % 1000000007


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]

        def move(row, col, moves):
            if moves < 0:
                return 0
            if not (0 <= row < m and 0 <= col < n):
                return 1

            if dp[row][col][moves] != -1:
                return dp[row][col][moves]

            up = move(row-1, col, moves-1)
            down = move(row+1, col, moves-1)
            left = move(row, col-1, moves-1)
            right = move(row, col+1, moves-1)

            dp[row][col][moves] = up + down + left + right
            return dp[row][col][moves]

        return move(startRow, startColumn, maxMove) % 1000000007


test = Solution()
test.findPaths(2, 2, 2, 0, 0)  # 6

test = Solution()
test.findPaths(1, 3, 3, 0, 1)  # 12
