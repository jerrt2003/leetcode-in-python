# -*- coding: utf-8 -*-
class Solution(object):
    def updateBoard(self, board, click):
        """
        Solution: BFS (172 ms)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/minesweeper/discuss/99826/Java-Solution-DFS-+-BFS
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        queue = [click]
        m = len(board)
        n = len(board[0])
        while queue:
            _curr_check = queue.pop()
            x = _curr_check[0]
            y = _curr_check[1]
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return board
            else:
                count = 0
                for i, j in [(x-1, y-1),(x, y-1),(x+1, y-1),(x-1, y),(x+1, y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
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
                            queue.append((i, j))
                            board[i][j] = 'B'
        return board