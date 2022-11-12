# -*- coding: utf-8 -*-
class Solution(object):
    def solve(self, board):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!!
        TP:
        - 首先找出可以被flip的"O"
        - 在每一次的recursion做完後flip "O" (免得先替換後後面同一次的iteration發現不能替換就尷尬了)
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return None
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        for i in range(self.row):
            for j in range(self.col):
                path = set()
                if self.modify(i, j, path):
                    for (x, y) in path:
                        self.board[x][y] = 'X'
        for i in board:
            print i

    def modify(self, i, j, path):
        if self.board[i][j] == 'X' or (i, j) in path:
            return True
        if (i == 0 or i == self.row-1 or j == 0 or j == self.col-1) and self.board[i][j] == 'O':
            return False
        path.add((i, j))
        if self.modify(i-1, j, path) and self.modify(i+1, j, path) and self.modify(i, j-1, path) and self.modify(i, j+1, path):
            return True
        else:
            return False
'''
board = [['X','X','X','X'],
         ['X','O','X','X'],
         ['X','X','O','X'],
         ['X','O','X','X']]
'''

'''
board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
'''

'''
[["O","X","X","O","X"],
 ["X","X","X","X","O"],
 ["X","X","X","O","X"],
 ["O","X","O","O","O"],
 ["X","X","O","X","O"]]
'''



board = [["X","O","O","X","X","X","O","X","O","O"],
         ["X","O","X","X","X","X","X","X","X","X"],
         ["X","X","X","X","O","X","X","X","X","X"],
         ["X","O","X","X","X","O","X","X","X","O"],
         ["O","X","X","X","O","X","O","X","O","X"],
         ["X","X","O","X","X","O","O","X","X","X"],
         ["O","X","X","O","O","X","O","X","X","O"],
         ["O","X","X","X","X","X","O","X","X","X"],
         ["X","O","O","X","X","O","X","X","O","O"],
         ["X","X","X","O","O","X","O","X","X","O"]]


sol = Solution()
sol.solve(board)