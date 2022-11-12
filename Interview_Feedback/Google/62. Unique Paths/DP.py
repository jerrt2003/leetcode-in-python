# -*- coding: utf-8 -*-
class Solution(object):
    def uniquePaths(self, m, n):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: MySELF!! (32ms, beat 80.93%)
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            DP[i][0] = 1
        for j in range(n):
            DP[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[-1][-1]