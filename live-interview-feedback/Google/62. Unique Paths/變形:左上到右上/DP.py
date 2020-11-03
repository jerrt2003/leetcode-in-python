# -*- coding: utf-8 -*-
class Solution(object):
    def uniquePath(self, m, n):
        DP = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if (i, j) == (0, 0):
                    DP[i][j] = 1
                else:
                    val1 = DP[i-1][j-1] if 0 <= i-1 and 0 <= j-1 else 0
                    val2 = DP[i][j-1] if 0 <= j-1 else 0
                    val3 = DP[i+1][j-1] if i+1 < m and 0 <= j-1 else 0
                    DP[i][j] = val1+val2+val3
        return DP[0][-1]

assert Solution().uniquePath(3,4) == 4