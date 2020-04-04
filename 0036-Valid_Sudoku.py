from __future__ import annotations


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = ["1","2","3","4","5","6","7","8","9",\
                    ".",".",".",".",".",".",".",".","."]
            for pos in row:
                if pos in nums:
                    nums.remove(pos)
                else:
                    # print("False in board1")
                    # return
                    return False

        board2 = map(list, zip(*board))
        for col in board2:
            nums = ["1","2","3","4","5","6","7","8","9",\
                    ".",".",".",".",".",".",".",".","."]
            for pos in col:
                if pos in nums:
                    nums.remove(pos)
                else:
                    # print("False in board2")
                    # return
                    return False

        board3 = []
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

        board3.append(chunk1)
        board3.append(chunk2)
        board3.append(chunk3)
        board3.append(chunk4)
        board3.append(chunk5)
        board3.append(chunk6)
        board3.append(chunk7)
        board3.append(chunk8)
        board3.append(chunk9)

        for chunk in board3:
            nums = ["1","2","3","4","5","6","7","8","9",\
                    ".",".",".",".",".",".",".",".","."]
            for pos in chunk:
                if pos in nums:
                    nums.remove(pos)
                else:
                    # print("False in board3")
                    # return
                    return False

        # print(True)
        # return
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
