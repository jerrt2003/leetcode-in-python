# -*- coding: utf-8 -*-
class Solution(object):
    def accumulateMatrix(self, matrix):
        for i in range(1, len(matrix)):
            matrix[i][0] += matrix[i-1][0]
        for j in range(1, len(matrix[0])):
            matrix[0][j] += matrix[0][j-1]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]+matrix[i][j]-matrix[i-1][j-1]
        return matrix

assert Solution().accumulateMatrix([[1, 2, 3],[1, 3, 5],[2, 4, 6]]) == [[1, 3, 6],[2, 7, 15],[4, 13, 27]]