# -*- coding: utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        """
        Solution: Using head column, row as flag
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/set-matrix-zeroes/discuss/26008/My-AC-java-O(1)-solution-(easy-to-read)
        TP:
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row_is_0 = False
        first_column_is_0 = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_is_0 = True
                    if j == 0:
                        first_column_is_0 = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        '''
        WHY we start with index 1?
        Ans: we might not need to change first row/column to 0 since matrix[i][0] or matrix[0][j] is 0 because other element in that row/column is 0
        '''
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_is_0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_column_is_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        print matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

sol = Solution()
sol.setZeroes(matrix)