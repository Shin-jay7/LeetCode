from __future__ import annotations
from collections import deque


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(board, idx):
            if idx < 0:
                return board
            left = right = idx
            while left > 0 and board[left-1] == board[idx]:
                left -= 1
            while right + 1 < len(board) and board[right+1] == board[idx]:
                right += 1
            balls = right - left + 1
            if balls >= 3:
                new_board = board[:left] + board[right+1:]
                return clean(new_board, left-1)
            else:
                return board

        hand = "".join(sorted(hand))
        q = deque([(board, hand, 0)])
        visited = set([(board, hand)])
        while q:
            board, hand, idx = q.popleft()
            for i in range(len(board)+1):
                for j in range(len(hand)):
                    if j > 0 and hand[j] == hand[j-1]:
                        continue
                    if i > 0 and board[i-1] == hand[j]:
                        continue
                    pick = False
                    if i < len(board) and board[i] == hand[j]:
                        pick = True
                    if 0 < i < len(board) and\
                       board[i-1] == board[i] and\
                       board[i] != hand[j]:
                        pick = True
                    if pick:
                        new_board = clean(
                             board[:i] + hand[j] + board[i:], i
                            )
                        new_hand = hand[:j] + hand[j+1:]
                        if not new_board:
                            return idx + 1
                        if (new_board, new_hand) not in visited:
                            q.append((new_board, new_hand, idx+1))
                            visited.add((new_board, new_hand))

        return -1
