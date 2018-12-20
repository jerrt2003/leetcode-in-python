# -*- coding: utf-8 -*-
class Solution(object):
    def solveSudoku(self, board):
        """
        Solution: Backtracking (Still feels like brutal force)
        Time Complexity: O(9^m) --> m: numbers of empty cells, each cell we can try 9 different numbers
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/sudoku-solver/discuss/15752/Straight-Forward-Java-Solution-Using-Backtracking
        TP:
        - The way to check if valid cell is from: Q.36
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.solve()
        print self.board


    def solve(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] != '.': continue
                else:
                    for num in range(1, 10):
                        self.board[i][j] = str(num)
                        if self.isRowValid(i) and self.isColValid(j) and self.isSecValid(i, j):
                            if self.solve():
                                return True # the next recursion return True which means this value for this cell is good, thus return True
                            else:
                                self.board[i][j] = '.'
                        else:
                            self.board[i][j] = '.'
                    return False # No number qualified for this cell, return False
        return True # will only hit this return when all empty cell filled with numbers which means we find the answer, thus return True

    def isRowValid(self, i):
        row = [x for x in self.board[i] if x != '.']
        if len(row) != len(set(row)): return False
        return True

    def isColValid(self, j):
        zip_board = zip(*self.board)
        col = [x for x in zip_board[j] if x != '.']
        if len(col) != len(set(col)): return False
        return True

    def isSecValid(self, i, j):
        if 0 <= i < 3:
            x = 0
        elif 3 <= i < 6:
            x = 3
        else:
            x = 6
        if 0 <= j < 3:
            y = 0
        elif 3 <= j < 6:
            y = 3
        else:
            y = 6
        sec_board = []
        for i in range(x, x+3):
            for j in range(y, y+3):
                sec_board.append(self.board[i][j])
        sec_board = [x for x in sec_board if x != '.']
        if len(sec_board) != len(set(sec_board)): return False
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)