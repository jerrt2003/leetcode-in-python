# -*- coding: utf-8 -*-
class Solution(object):
    def maximalSquare(self, matrix):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity: O(1)
        Perf: Runtime: 400 ms, faster than 6.08% / Memory Usage: 16.1 MB, less than 61.86%
        Inspired By: MySELF!!
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.res = 0

        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] != '0':
                    self.res = max(self.res, 1*1)
                    self.dfs(i+1, j+1, i, j, matrix)
        return self.res

    def dfs(self, i, j, start_i, start_j, matrix):
        if i >= self.m or j >= self.n:
            return
        for k in range(start_i, i + 1):
            if matrix[k][j] != '1':
                return
        for k in range(start_j, j + 1):
            if matrix[i][k] != '1':
                return
        self.res = max(self.res, pow(i - start_i + 1, 2))
        self.dfs(i + 1, j + 1, start_i, start_j, matrix)