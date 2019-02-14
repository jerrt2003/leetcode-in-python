# -*- coding: utf-8 -*-
class Solution(object):
    def numDistinct(self, s, t):
        """
        Solution: DP
        Time Complexity: O(n^2)
        Space Complexity: O(mn)
        Inspired By: https://www.youtube.com/watch?v=mPqqXh8XvWY&t=252s
        Perf: Runtime: 104 ms, faster than 58.10% / Memory Usage: 15.2 MB, less than 100.00%
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)+1
        n = len(t)
        DP = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            DP[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if s[j-1] == t[i-1]:
                    DP[i][j] = DP[i-1][j-1] + DP[i][j-1]
                else:
                    DP[i][j] = DP[i][j-1]
        return DP[-1][-1]