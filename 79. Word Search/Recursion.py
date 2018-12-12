# -*- coding: utf-8 -*-
class Solution(object):
    def exist(self, board, word):
        """
        Solution: backtracking
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        TP:
        - basically we need to check each character for all possible directions
        - !!!!! Python function object is PASS BY REFERENCE !!!!!
            - thus when we pass "visited" into recursion, we need to either COPY the list(support after 3.x) or slice it (visited[:])
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.len_column = len(board)
        self.len_raw = len(board[0])
        self.word = list(word)
        self.len_word = len(word)
        for i in range(self.len_column):
            for j in range(self.len_raw):
                if self.checkIfExisted(i, j, [], idx=0):
                    return True
        return False

    def checkIfExisted(self, i, j, visited, idx=None):
        if (i, j) in visited:
            return False
        char = self.word[idx]
        if char == self.board[i][j]:
            visited.append((i,j))
            if idx+1 == self.len_word:
                return True
            elif i+1 < self.len_column and self.checkIfExisted(i+1, j, visited[:], idx=idx+1):
                return True
            elif 0 < i and self.checkIfExisted(i-1, j, visited[:], idx=idx+1):
                return True
            elif j+1 < self.len_raw and self.checkIfExisted(i, j+1, visited[:], idx=idx+1):
                return True
            elif 0 < j and self.checkIfExisted(i, j-1, visited[:], idx=idx+1):
                return True
        else:
            return False
'''
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
'''

board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]
word = "ABCESEEEFS"

#board = [["a"],["a"]]
#word = "aaa"

sol = Solution()
print sol.exist(board, word)