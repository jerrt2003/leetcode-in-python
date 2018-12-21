# -*- coding: utf-8 -*-
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        for i in range(n):
            for j in range(n):
                board = [['.' for _ in range(n)] for _ in range(n)]
                board[i][j] = 'Q'
                if self.solve(board, n-1):
                    if not board in res:
                        res.append(board)
        final_res = []
        for result in res:
            a = [''.join(x) for x in result]
            final_res.append(a)
        return final_res

    def solve(self, board, queen_num):
        if queen_num == 0:
            return True # all queens being placed already. Return True
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.': continue
                board[i][j] = 'Q'
                if self.isValid(board, i, j):
                    if self.solve(board, queen_num-1):
                        return True
                    else:
                        board[i][j] = '.'
                else:
                    board[i][j] = '.'
        return False


    def isValid(self, board, i, j):
        # check if row is valid
        row = [x for x in board[i] if x != '.']
        if len(row) > 1:
            return False
        # check if col is valid
        check_board = zip(*board)
        col = [x for x in check_board[j] if x != '.']
        if len(col) > 1:
            return False
        # check diagonal is valid
        # top-left-directions
        x, y = i, j
        while x-1 >= 0 and y-1 >= 0:
            if board[x-1][y-1] == 'Q':
                return False
            else:
                x -= 1
                y -= 1
        # top-right
        x, y = i, j
        while x+1 < len(board) and y-1 >= 0:
            if board[x+1][y-1] == 'Q':
                return False
            else:
                x += 1
                y -= 1
        # bottom-left
        x, y = i, j
        while x-1 >= 0 and y+1 < len(board):
            if board[x-1][y+1] == 'Q':
                return False
            else:
                x -= 1
                y += 1
        # bottom-right
        x, y = i, j
        while x+1 < len(board) and y+1 < len(board):
            if board[x+1][y+1] == 'Q':
                return False
            else:
                x += 1
                y += 1
        return True

print Solution().solveNQueens(5)