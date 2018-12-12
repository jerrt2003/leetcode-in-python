# -*- coding: utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Solution: O(M*N) search
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        Inspired By: MySELF!!
        - Check Solution in Q.240
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix)==0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False

        row = 0
        col = len(matrix[0])-1
        while row < len(matrix) and col > -1:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 99

print Solution().searchMatrix(matrix, target)