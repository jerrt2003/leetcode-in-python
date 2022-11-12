# -*- coding: utf-8 -*-
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        dir = -1, 1
        i, j = 0, 0
        m, n, res = len(matrix), len(matrix[0]), []
        while len(res) < m*n:
            res.append(matrix[i][j])
            i, j = i+dir[0], j+dir[1]
            if j < 0 or j >= n or i < 0 or i >= m:
                if j < 0 and i < m:
                    i, j = i, j+1
                elif j < 0 and i >= m:
                    i, j = i-1, j+2
                elif j < n and i >= m:
                    i, j = i-1, j+2
                elif i < 0 and j < n:
                    i, j = i+1, j
                elif i < 0 and j >= n:
                    i, j = i+2, j-1
                elif i < m and j >= n:
                    i, j = i+2, j-1
                dir = -1*dir[0], -1*dir[1]
        return res

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

assert Solution().findDiagonalOrder(matrix) == [1,2,4,7,5,3,6,8,9]

matrix = [
 [ 1, 2, 3, 4 ],
 [ 4, 6, 7, 8 ],
 [ 9, 10, 11, 12 ]
]

assert Solution().findDiagonalOrder(matrix) == [1,2,4,9,6,3,4,7,10,11,8,12]

