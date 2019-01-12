# -*- coding: utf-8 -*-
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def DFS(i, j, path, wordSoFar, word, board, m, n):
            ans = ''.join(wordSoFar)
            if ans == word:
                return True
            neighbor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i_dir, j_dir in neighbor:
                x, y = i + i_dir, j+j_dir
                if not (x, y) in path and 0 <= x < m and 0 <= y < n:
                    if DFS(x, y, path + [(x, y)], wordSoFar + [board[x][y]], word, board, m, n):
                        return True
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if DFS(i, j, [], [], word, board, m, n):
                    return True
        return False


