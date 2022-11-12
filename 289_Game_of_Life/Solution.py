# -*- coding: utf-8 -*-
class Solution(object):
    def gameOfLife(self, board):
        """
        Solution: Go through board
        Time Complexity: O(mn)
        Space Complexity: O(1)
        TP:
        - Go through each cell to count each cells live/dead neighbor to decide its state then mark it
        - live condition:
            - Any live cell with two or three live neighbors lives on to the next generation
            - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        - die condition:
            - Any live cell with fewer than two live neighbors dies, as if caused by under-population
            - Any live cell with more than three live neighbors dies, as if by over-population
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.nnb(board, i, j) == 3:
                        board[i][j] = 2
                else:
                    if self.nnb(board, i, j) < 2 or self.nnb(board, i, j) > 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0
        print board

    def nnb(self, board, i, j):
        m, n = len(board), len(board[0])
        count = 0
        if i - 1 >= 0 and j - 1 >= 0:
            count += board[i - 1][j - 1] % 2
        if i - 1 >= 0:
            count += board[i - 1][j] % 2
        if i - 1 >= 0 and j + 1 < n:
            count += board[i - 1][j + 1] % 2
        if j - 1 >= 0:
            count += board[i][j - 1] % 2
        if j + 1 < n:
            count += board[i][j + 1] % 2
        if i + 1 < m and j - 1 >= 0:
            count += board[i + 1][j - 1] % 2
        if i + 1 < m:
            count += board[i + 1][j] % 2
        if i + 1 < m and j + 1 < n:
            count += board[i + 1][j + 1] % 2
        return count

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

sol = Solution()
sol.gameOfLife(board)