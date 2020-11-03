class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.row = [0] * n
        self.col = [0] * n
        self.diagnoal = 0
        self.anti_diagnoal = 0

    def move(self, row, col, player):
        """
        Facebook
        T:O(1) S:O(mn)
        Runtime: 68 ms, faster than 99.59% of Python online submissions for Design Tic-Tac-Toe.
        Memory Usage: 14.8 MB, less than 65.50% of Python online submissions for Design Tic-Tac-Toe.
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.diagnoal += 1
            if row + col == self.n - 1:
                self.anti_diagnoal += 1
            if self.row[row] == self.n or self.col[
                col] == self.n or self.diagnoal == self.n or self.anti_diagnoal == self.n:
                return 1
        elif player == 2:
            self.row[row] += -1
            self.col[col] += -1
            if row == col:
                self.diagnoal += -1
            if row + col == self.n - 1:
                self.anti_diagnoal += -1
            if self.row[row] == -self.n or self.col[
                col] == -self.n or self.diagnoal == -self.n or self.anti_diagnoal == -self.n:
                return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)