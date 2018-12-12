# -*- coding: utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """

        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0: return False
        left = 0
        right = len(matrix) - 1
        if target < matrix[left][0] or target > matrix[right][len(matrix[0])-1]: return False
        while right >= left:
            mid = (left+right)/2
            if matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid+1
        end = right
        for i in range(end+1):
            left = 0
            right = len(matrix[0])-1
            while left <= right:
                mid = (left + right)/2
                if matrix[i][mid] > target:
                    right = mid-1
                elif matrix[i][mid] < target:
                    left = mid+1
                else:
                    return True
        return False

'''
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''

matrix = [[-5]]

target = -5

print Solution().searchMatrix(matrix, target)