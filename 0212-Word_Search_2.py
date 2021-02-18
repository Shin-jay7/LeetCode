from __future__ import annotations


class Node:
    def __init__(self):
        self.chars = {}
        self.word = False

class Trie:
    def __init__(self):
        self.node = Node()

    def add_word(self, word):
        node = self.node
        for char in word:
            if char not in node.chars:
                node.chars[char] = Node()
            node = node.chars[char]
        node.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie = Trie()

        for word in words:
            trie.add_word(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.node, ans, "", i, j)
        
        return ans

    def dfs(self, board, trie, ans, word, i, j):
        if trie.word:
            ans.append(word)
            trie.word = False
        if i < 0 or i>= len(board) or j < 0 or j >= len(board[0]):
            return
        if not trie:
            return
        char = board[i][j]
        if char in trie.chars:
            board[i][j] = '#'
            trie = trie.chars[char]
            for x, y in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                self.dfs(board, trie, ans, word + char, i + x, y + j)
            board[i][j] = char


"""
one-dimensional dictionary where the keys are complex numbers representing
the row/column indexes. That makes further work with it easier. 
Looping over all board positions is just for z in board, the four neighbors
of a board position z are just z + 1j**k (for k in 0 to 3), and I don't need
to check borders because board.get just returns "None" if I request an invalid
position.
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[''] = word
        board = {i + 1j*j: char
                 for i, row in enumerate(board)
                 for j, char in enumerate(row)}
        ans = []

        def search(node, z):
            if '' in node:
                ans.append(node.pop(''))
            char = board.get(z)
            if char in node:
                board[z] = '#'
                for k in range(4):
                    search(node[char], z + 1j**k)
                board[z] = char

        for z in board:
            search(trie, z)

        return ans
