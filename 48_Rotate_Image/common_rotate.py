# -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        Solution: Common Rotate
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
        TP:
        (clock wise)
        - 先上下reverse, 再對角線互換
        - first reverse the matrix
        - then we swap the diagonal element (e.g. matrix[i][j] = matrix[j][i])
        (counter-clock wise)
        - 先左右reverse, 在對角線互換
        - first reverse left to right
        - then swap diagonal
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix = matrix[::-1]
        matrix_len = len(matrix)
        for i in range(matrix_len):
            for j in range(i+1, matrix_len):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        return matrix

input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

sol = Solution()
print sol.rotate(input)
