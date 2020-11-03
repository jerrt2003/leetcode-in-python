# -*- coding: utf-8 -*-
class Soltuion(object):
    def Solution(self, matrix):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        :param matrix:
        :return:
        """
        m = len(matrix)
        n = len(matrix[0])
        DP = [[float('inf') for _ in range(n)] for _ in range(m)]
        DP[0][0] = matrix[0][0]
        for i in range(1,m):
            DP[i][0] = min(DP[i-1][0], matrix[i][0])
        for j in range(1, n):
            DP[0][j] = min(DP[0][j-1], matrix[0][j])
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = max(min(DP[i-1][j], matrix[i][j]), min(DP[i][j-1], matrix[i][j]))
        return DP[-1][-1]

matrix = [[8,4,7],[6,5,9]]
print Soltuion().Solution(matrix)