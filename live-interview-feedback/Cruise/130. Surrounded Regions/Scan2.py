# -*- coding: utf-8 -*-
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.visit = set()
        self.toBeFlip = list()

        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == 'O' and (i, j) not in self.visit:
                    self.flip = True
                    path = []
                    self.dfs(i, j, path)
                    if self.flip:
                        self.toBeFlip.extend(path)

        for (i, j) in self.toBeFlip:
            self.board[i][j] = 'X'

    def dfs(self, i, j, path):
        self.visit.add((i, j))
        path.append((i, j))
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if x < 0 or x >= self.m or y < 0 or y >= self.n:
                self.flip = False
            elif (x, y) not in self.visit and self.board[x][y] == 'O':
                self.dfs(x, y, path)


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)