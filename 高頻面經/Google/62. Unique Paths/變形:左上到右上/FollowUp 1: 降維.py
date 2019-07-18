# -*- coding: utf-8 -*-
class Solution(object):
    """
    Time Complexity: O(mn)
    Space Complexity: O(m)
    """
    def uniquePath(self, m, n):
        DP = [0 for _ in range(m)]
        for j in range(n):
            tmpDP = DP[:]
            for i in range(m):
                if (i, j) == (0, 0):
                    DP[i] = 1
                else:
                    val1 = tmpDP[i-1] if 0 <= i-1 and 0 <= j-1 else 0
                    val2 = tmpDP[i] if 0 <= j-1 else 0
                    val3 = tmpDP[i+1] if i+1 < m and 0 <= j-1 else 0
                    DP[i] = val1+val2+val3
        return DP[0]

assert Solution().uniquePath(3,4) == 4