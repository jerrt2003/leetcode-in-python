# -*- coding: utf-8 -*-
class Solution(object):
    def gameOfLife(self, board):
        """
        Solution: O(m*n)
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        TP:
        - live condition:
            - Any live cell with two or three live neighbors lives on to the next generation
            - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        - die condition:
            - Any live cell with fewer than two live neighbors dies, as if caused by under-population
            - Any live cell with more than three live neighbors dies, as if by over-population
        - 0: dead cell
        - 1: live cell
        - 2: dead cell which will be live in the next round
        - 3: live cell which will be dead in next round
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def checkNeighborStatus(i, j, board):
            dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            count = 0
            for x_dir, y_dir in dirs:
                x, y = i + x_dir, j + y_dir
                if 0 <= x < m and 0 <= y < n: #!!!
                    count += board[x][y] % 2
                    """
                    if neighbor is dead (0) --> then board[x][y] % 2 = 0 --> 
                    if neighbor will be dead to live (2) --> then board[x][y] % 2 = 0 --> still indicate that this cell is dead at this round
                    """
            return count

        if board:
            m, n = len(board), len(board[0])
            for i in range(m):
                for j in range(n):
                    """
                    We only mark the cell which are going to have status change. For those doesn't change in next round, we'll leave it as is
                    """
                    neightborCount = checkNeighborStatus(i, j, board)
                    if board[i][j] == 0:
                        if neightborCount == 3:
                            board[i][j] = 2
                    else:
                        if neightborCount < 2 or neightborCount > 3:
                            board[i][j] = 3
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 2:
                        board[i][j] = 1
                    elif board[i][j] == 3:
                        board[i][j] = 0

