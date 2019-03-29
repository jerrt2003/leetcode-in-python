# -*- coding: utf-8 -*-
import collections
class NumMatrix(object):

    def __init__(self, matrix):
        """
        Solution: 2D DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 228 ms, faster than 45.77% / Memory Usage: 14 MB, less than 9.52%
        Inspired By: MySELF!!
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return None
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.DP = [[0 for _ in range(self.n+1)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n+1):
                if j == 0:
                    self.DP[i][j] = 0
                else:
                    self.DP[i][j] = matrix[i][j-1] + self.DP[i][j-1]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        orig = self.matrix[row][col]
        diff = val - orig
        for j in range(col+1, self.n+1):
            self.DP[row][j] += diff
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2+1):
            _col_sum = self.DP[i][col2+1] - self.DP[i][col1]
            res += _col_sum
        return res





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)