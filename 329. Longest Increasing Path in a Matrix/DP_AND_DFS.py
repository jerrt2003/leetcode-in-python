# -*- coding: utf-8 -*-
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        Solution: DFS + DP
        Time Complexity: O(mn)
        Space Complexity: O(mn)
        Inspired By: ...should be MySELF!! but old code is TLE
        TP:
        - basic idea will be doing DFS and increase the path len as much as possible
        - but it will help if we have DP so it will have constant time
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0: return 0
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.matrix = matrix
        self.DP = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.DP[i][j] = self.findLongest(i, j)
        return max(self.DP[i][j] for i in range(self.row) for j in range(self.col))


    def findLongest(self, i, j):
        if self.DP[i][j] == 0:
            val = self.matrix[i][j]
            len_go_up = self.findLongest(i-1, j) if i > 0 and val < self.matrix[i-1][j] else 0
            len_go_down = self.findLongest(i+1, j) if i < self.row -1 and val < self.matrix[i+1][j] else 0
            len_go_left = self.findLongest(i, j-1) if j > 0 and val < self.matrix[i][j-1] else 0
            len_go_right = self.findLongest(i, j+1) if j < self.col -1 and val < self.matrix[i][j+1] else 0
            self.DP[i][j] = 1 + max(len_go_up,len_go_down,len_go_left,len_go_right)
        return self.DP[i][j]

nums = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]

sol = Solution()
print sol.longestIncreasingPath(nums)