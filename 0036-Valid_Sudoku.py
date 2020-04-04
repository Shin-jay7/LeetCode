from __future__ import annotations


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board2 = map(list, zip(*board))

        board3 = []
        for i in [0,3,6]:
            for j in [0,3,6]:
                chunk = [board[x][y] for x in range(i,i+3)\
                                      for y in range(j,j+3)]
                board3.append(chunk)

        # print(self.board_checker(board) and self.board_checker(board2)\
        #       and self.board_checker(board3))
        # return
        return self.board_checker(board) and self.board_checker(board2)\
               and self.board_checker(board3)

    def board_checker(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = ["1","2","3","4","5","6","7","8","9",\
                    ".",".",".",".",".",".",".",".","."]
            for pos in row:
                if pos in nums:
                    nums.remove(pos)
                else:
                    return False
        return True


test = Solution()
test.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) # True

test = Solution()
test.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) # False

test = Solution()
test.isValidSudoku([
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]) # False
