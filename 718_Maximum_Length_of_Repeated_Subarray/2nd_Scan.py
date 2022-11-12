# -*- coding: utf-8 -*-
class Solution(object):
    def findLength(self, A, B):
        """
        Solution: 2D-DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 4360 ms, faster than 15.64% / Memory Usage: 32.7 MB, less than 24.00%
        Inspired By: MySELF!!
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A) + 1, len(B) + 1
        DP = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(1, m):
            for j in range(1, n):
                if A[i - 1] == B[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                    res = max(res, DP[i][j])
        return res
