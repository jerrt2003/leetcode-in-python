# -*- coding: utf-8 -*-
class Solution(object):
    def isValidSudoku(self, board):
        """
        Solution: Hash + Set
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution
        TP:
        - 利用set的特性去fiter out重複的數字
        - 利用zip function去把每一個column給串起來
        - 把每個小squre串成一個list去檢查是否有重複
        :type board: List[List[str]]
        :rtype: bool
        """
        if self.check_if_each_row_is_valid(board) and self.check_if_each_column_is_valid(board) and self.check_if_each_cell_is_valid(board):
            return True
        return False

    def check_if_each_row_is_valid(self, board):
        for row in board:
            if not self.isValid(row):
                return False
        return True

    def check_if_each_column_is_valid(self, board):
        for column in zip(*board): # using zip to "zip" each column into a tuple
            if not self.isValid(column):
                return False
        return True

    def check_if_each_cell_is_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                sqaure = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)] # put all 9 small board values into one list
                if not self.isValid(sqaure):
                    return False
        return True

    def isValid(self, unit):
        a = [x for x in unit if x != '.']
        return len(a) == len(set(a)) # using set to filter out duplicates

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print sol.isValidSudoku(board)