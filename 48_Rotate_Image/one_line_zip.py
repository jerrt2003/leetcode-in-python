# -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix = [list(A)[::-1] for A in zip(*matrix)]


input = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

print Solution().rotate(input)