# -*- coding: utf-8 -*-
class Solution(object):
    def maxSumSubmatrix(self, matrix):
        """
        Sub problem: To find maximum sum of rectangular sub-array from a 2-D array
        Solution: DP
        Time Complexity: O(m*n*n)
        Space Complexity: O(n)
        Inspired By: https://www.youtube.com/watch?v=yCQN096CwWM
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def findMaxSum(array):
            """
            To find the maximum subarray of given array
            :param array:
            :return: sum, i, j
            """
            maxSoFar = maxEndHere = array[0]
            for i in range(1, len(array)):
                maxEndHere = max(maxEndHere+array[i], array[i])
                maxSoFar = max(maxSoFar, maxEndHere)
            return maxSoFar

        len_row = len(matrix)
        len_col = len(matrix[0])
        MAX = 0
        for i in range(len_row):
            sum_row = [0 for _ in range(len_col)]
            for j in range(i, len_row):
                sum_row = [x + y for x, y in zip(sum_row, matrix[j])]
                MAX = max(MAX, findMaxSum(sum_row))
        return MAX

matrix = [[ 2,  1, -3, -4,  5],
          [ 0,  6,  3,  4,  1],
          [ 2, -2, -1,  4, -5],
          [-3,  3,  1,  0,  3]]

print Solution().maxSumSubmatrix(matrix)