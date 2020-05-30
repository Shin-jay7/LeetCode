from __future__ import annotations

"""
1) Find 'O' in the surrounding boarder
2) Change 1) and its neighbor 'O' (or 'O's) to '*'
3) Replace all the remaining '0' with 'X'
4) Return '*' to '0'
"""
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]: return

        queue = deque([])
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and\
                    board[r][c] == "O":
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "*"
                queue.append((r-1, c))
                queue.append((r+1, c))
                queue.append((r, c-1))
                queue.append((r, c+1))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "*":
                    board[r][c] = "O"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]: return

        rows, cols = len(board), len(board[0])

        save = [rc for i in range(max(rows,cols))\
                    for rc in ((0,i), (rows-1,i), (i,0), (i,cols-1))]

        while save:
            r, c = save.pop()
            if 0 <= i < rows and 0 <= j < cols and board[r][c] == 'O':
                board[r][c] = '*'
                save += (r,c-1), (r,c+1), (r-1,c), (r+1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "*":
                    board[r][c] = "O"
