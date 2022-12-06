from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ret: List[List[str]] = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.dfs(0, board)
        return self.ret
        
    
    def dfs(self, row: int, board: List[List[str]]) -> None:
        # 終止條件: row == len(board)
        if row == len(board):
            tmp: List[str] = []
            for row_element in board:
                tmp.append("".join(row_element))
            self.ret.append(tmp)
            return
        # 在該行中每個位置(col)的位置嘗試放置Q
        for col in range(len(board)):
            # 驗證放Q是否合法
            if self.is_valid(row, col, board): 
                # 放Q
                board[row][col] = 'Q'
                # 轉往下一列
                self.dfs(row+1, board)
                # 回朔：把Q拿走
                board[row][col] = '.'

    def is_valid(self, row: int, col: int, board: List[List[str]]) -> bool:
        # 同一col 是否衝突？
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 左上角是否衝突？
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 右上角是否衝突？
        i, j = row-1, col+1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True