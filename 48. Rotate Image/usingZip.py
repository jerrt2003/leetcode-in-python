# -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        Solution: zip
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
        TP:
        - reversed the matrix
        - Using ZIP to "zip" all column together
        - Remember to transfer tuple to the list
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix = zip(*matrix[::-1])
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])
        print matrix


input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

sol = Solution()
sol.rotate(input)