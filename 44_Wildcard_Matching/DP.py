# -*- coding: utf-8 -*-
class Solution(object):
    def isMatch(self, s, p):
        """
        Solution: 2D-DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 1256 ms, faster than 29.16% / Memory Usage: 19.6 MB, less than 25.00%
        Inspired By:
        - MySELF!!
        - https://www.youtube.com/watch?v=3ZDZ-N0EPV0
        TP:
        - if pattern == '*', the DP[i][j] = DP[i-1][j] || DP[i][j-1]
        - DP[i-1][j] means '*' stands for empty string
        - DP[i][j-1] means we use '*' to include the last character of string
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)+1
        n = len(p)+1
        DP = [[False for _ in range(m)] for _ in range(n)]
        # init DP
        DP[0][0] = True
        for j in range(1, m):
            DP[0][j] = False
        for i in range(1, n):
            if p[i-1] != '*':
                DP[i][0] = False
            else:
                DP[i][0] = DP[i-1][0]
        for i in range(1, n):
            for j in range(1, m):
                idx_i, idx_j = i-1, j-1
                if s[idx_j] == p[idx_i] or p[idx_i] == '?':
                    DP[i][j] = DP[i-1][j-1]
                elif p[idx_i] == '*':
                    DP[i][j] = DP[i-1][j] or DP[i][j-1] #!!!!!
        return DP[-1][-1]

s = 'cb'
p = '?a'
print Solution().isMatch(s, p)