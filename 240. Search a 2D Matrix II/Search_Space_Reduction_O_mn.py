# -*- coding: utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        Solution: Search Space
        Time Complexity: O(mn)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
        TP:
        - start from top-right corner (e.g. matrix[i][j])
        - if target < matrix[i][j]
            - means the target won't be in this "col", so we can exclude this one (e.g. col -= 1)
        - elif target > matrix[i][j]
            - means the target won't be in this "row", so we can exclude this row (e.g. row += 1)
        - continue this logic until we find the target, else return False
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0: return False
        row = 0
        col = len(matrix[0])-1
        while row < len(matrix) and col > -1:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False

#matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
matrix = []
target = -1

print Solution().searchMatrix(matrix, target)