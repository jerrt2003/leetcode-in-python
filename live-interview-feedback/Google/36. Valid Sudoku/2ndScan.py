# -*- coding: utf-8 -*-
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isRowValid():
            for row in board:
                _row = [a for a in row if a != '.']
                if len(_row) != len(set(_row)):
                    return False
            return True

        def isColValid():
            for col in zip(*board):
                _col = [a for a in col if a != '.']
                if len(_col) != len(set(_col)):
                    return False
            return True

        def isCellValid():
            start_i = (0, 3, 6)
            start_j = (0, 3, 6)
            for i in start_i:
                for j in start_j:
                    cell = []
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            if board[x][y] != '.':
                                cell.append(board[x][y])
                    if len(cell) != len(set(cell)):
                        return False
            return True

        return isRowValid() and isColValid() and isCellValid()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
assert Solution().isValidSudoku(board)