from __future__ import annotations


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.initBoard(board)
        self.solve()

    def initBoard(self, board):
        self.board = board
        self.unassigned_pos = set([(r_idx,c_idx) for r_idx in range(9)\
                                                 for c_idx in range(9)\
                                  if self.board[r_idx][c_idx] == "."])

        self.nums = [[set("123456789") for c_idx in range(9)] for r_idx in range(9)]
        for r_idx in range(9):
            for c_idx in range(9):
                num = self.board[r_idx][c_idx]
                if num != ".":
                    self.nums[r_idx][c_idx] = set()
                    self.update_nums((r_idx,c_idx), num)

    def solve(self):
        if not self.unassigned_pos:
            return True

        # find the position with fewest candidates
        pos = min(self.unassigned_pos, key=lambda pos: len(self.nums[pos[0]][pos[1]]))

        # fill the position with one of the candidates and solve recursively
        r_idx, c_idx = pos
        for num in list(self.nums[r_idx][c_idx]):
            updated_positions = self.fill_pos(pos, num)
            if self.solve():
                return True
            self.unfill_pos(pos, num, updated_positions)

        # if no solution found, go back and try the next canidate
        return False

    def fill_pos(self, pos, num):
        r_idx, c_idx = pos
        self.board[r_idx][c_idx] = num

        self.unassigned_pos.remove(pos)
        updated_positions = self.update_nums(pos, num)

        return updated_positions

    def unfill_pos(self, pos, num, updated_positions):
        r_idx, c_idx = pos
        self.board[r_idx][c_idx] = "."
        self.unassigned_pos.add(pos)

        for r_idx, c_idx in updated_positions:
            self.nums[r_idx][c_idx].add(num)

    def update_nums(self, filled_pos, num):
        updated_positions = []
        for r_idx, c_idx in self.related_pos(filled_pos):
            if (self.board[r_idx][c_idx] == ".") and (num in self.nums[r_idx][c_idx]):
               self.nums[r_idx][c_idx].remove(num)
               updated_positions.append((r_idx, c_idx))
        return updated_positions

    def related_pos(self, pos):
        return list(set(self.same_row(pos) + self.same_col(pos) + self.same_square(pos)))

    def same_row(self, pos):
        return [(pos[0], c_idx) for c_idx in range(9)]

    def same_col(self, pos):
        return [(r_idx, pos[1]) for r_idx in range(9)]

    def same_square(self, pos):
        first_r_idx = (pos[0] // 3) * 3
        first_c_idx = (pos[1] // 3) * 3
        return [
            (first_r_idx + square_r_idx, first_c_idx + square_c_idx)\
            for square_r_idx in range(3) for square_c_idx in range(3)
        ]
