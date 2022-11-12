# -*- coding: utf-8 -*-
class Solution(object):
    def updateBoard(self, board, click):
        """
        Solution: DFS (180 ms)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/minesweeper/discuss/99826/Java-Solution-DFS-+-BFS
        TP:
            - If click on a mine ('M'), mark it as 'X', stop further search.
            - If click on an empty cell ('E'), depends on how many surrounding mine:
                - Has surrounding mine(s), mark it with number of surrounding mine(s), stop further search.
                - No surrounding mine, mark it as 'B', continue search its 8 neighbors.
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        m = len(board)
        n = len(board[0])
        x = click[0]
        y = click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            count = 0
            for i, j in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
                if i < 0 or i >= m or j < 0 or j >= n: continue
                if board[i][j] == 'M' or board[i][j] == 'X':
                    count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for i, j in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1),
                             (x, y + 1), (x + 1, y + 1)]:
                    if i < 0 or i >= m or j < 0 or j >= n: continue
                    if board[i][j] == 'E':
                        self.updateBoard(board, (i, j))
        return board