from __future__ import annotations


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True

        return False

    def dfs(self, board, row, col, word, idx):
        if idx == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if board[row][col] != word[idx]:
            return False

        char = board[row][col]
        board[row][col] = " "
        ans = self.dfs(board, row+1, col, word, idx+1) or\
              self.dfs(board, row-1, col, word, idx+1) or\
              self.dfs(board, row, col+1, word, idx+1) or\
              self.dfs(board, row, col-1, word, idx+1)
        board[row][col] = char

        return ans


test = Solution()
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
test.exist(board, "ABCCED") # True
test.exist(board, "SEE") # True
test.exist(board, "ABCB") # False
