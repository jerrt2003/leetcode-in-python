# -*- coding: utf-8 -*-
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or len(matrix) == 0:
            return
        m = len(matrix)+1
        n = len(matrix[0])+1
        self.DP = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                self.DP[i][j] = self.DP[i-1][j] + self.DP[i][j-1] - self.DP[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 40 ms, faster than 82.62% / Memory Usage: 13.5 MB, less than 12.00%
        Inspired By:
        - https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75430/DP-Java-solution
        - https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.DP is None:
            return 0
        res = self.DP[row2+1][col2+1] - self.DP[row1][col2+1] - self.DP[row2+1][col1] + self.DP[row1][col1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)