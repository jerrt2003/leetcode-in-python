class Solution(object):
    def candyCrush(self, board):
        """
        Facebook
        T:O(mn) S:O(mn)
        Runtime: 152 ms, faster than 81.86% of Python online submissions for Candy Crush.
        Memory Usage: 12.8 MB, less than 54.42% of Python online submissions for Candy Crush.
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        while True:
            crush = set()
            for i in range(m):
                for j in range(n):
                    if i > 1 and board[i][j] != 0 and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}
                    if j > 1 and board[i][j] != 0 and board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
            if not crush:
                break
            for i, j in crush:
                board[i][j] = 0
            for j in range(n):
                idx = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j]:
                        board[idx][j] = board[i][j]
                        idx -= 1
                for i in range(idx + 1):
                    board[i][j] = 0

        return board

print Solution().candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]])