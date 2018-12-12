# -*- coding: utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        """
        Solution: O(m+n) space complexity
        Time Complexity: O(mn)
        Space Complexity: O(m+n)
        Inspired By: https://leetcode.com/problems/set-matrix-zeroes/solution/
        TP:
        - Go through the matrix and mark element's i, j if element is 0
        - Go through the matrix again and flip element if element's i, j in the marked row, column set
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        column = []
        row = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    column.append(j)
                    row.append(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                    matrix[i][j] = 0
        print matrix

matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

sol = Solution()
sol.setZeroes(matrix)