from __future__ import annotations


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def board_checker(board: List[List[str]]) -> bool:
            for row in board:
                nums = ["1","2","3","4","5","6","7","8","9",\
                        ".",".",".",".",".",".",".",".","."]
                for pos in row:
                    if pos in nums:
                        nums.remove(pos)
                    else:
                        return False
            return True

        board2 = map(list, zip(*board))

        chunk1, chunk2, chunk3 = [], [], []
        chunk4, chunk5, chunk6 = [], [], []
        chunk7, chunk8, chunk9 = [], [], []
        for index,row in enumerate(board):
            if index in [0,1,2]:
                for idx,pos in enumerate(row):
                    if idx in [0,1,2]:
                        chunk1.append(pos)
                    elif idx in [3,4,5]:
                        chunk2.append(pos)
                    else:
                        chunk3.append(pos)
            elif index in [3,4,5]:
                for idx,pos in enumerate(row):
                    if idx in [0,1,2]:
                        chunk4.append(pos)
                    elif idx in [3,4,5]:
                        chunk5.append(pos)
                    else:
                        chunk6.append(pos)
            else:
                for idx,pos in enumerate(row):
                    if idx in [0,1,2]:
                        chunk7.append(pos)
                    elif idx in [3,4,5]:
                        chunk8.append(pos)
                    else:
                        chunk9.append(pos)

        board3 = [chunk1,chunk2,chunk3,chunk4,chunk5,chunk6,chunk7,chunk8,chunk9]

        # print(board_checker(board) and board_checker(board2) and board_checker(board3))
        # return
        return board_checker(board) and board_checker(board2) and board_checker(board3)


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
