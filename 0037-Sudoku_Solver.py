from __future__ import annotations


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.state = {str(x): 0 for x in range(1,10)}
        self.initState()
        self.solve()

    def initState(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != ".":
                    self.state[self.board[row][col]] += 1

    def solve(self):
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True

        for num in set([x for x in self.state if self.state[x] != 9]):
            if self.isValid(row, col, num):
                self.board[row][col] = num
                self.state[num] += 1
                if self.solve():
                    return True
                self.board[row][col] = "."
                self.state[num] -= 1
        return False

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def isValid(self, row, col, check_num):
        boxrow = row - row%3
        boxcol = col - col%3
        if self.isValidRow(row,check_num) and\
           self.isValidCol(col,check_num) and\
           self.isValidSquare(boxrow, boxcol, check_num):
            return True
        return False

    def isValidRow(self, row, check_num):
        for col in range(9):
            if self.board[row][col] == check_num:
                return False
        return True

    def isValidCol(self, col, check_num):
        for row in range(9):
            if self.board[row][col] == check_num:
                return False
        return True

    def isValidSquare(self, row, col, check_num):
        for r in range(row,row+3):
            for c in range(col, col+3):
                if self.board[r][c] == check_num:
                    return False
        return True
