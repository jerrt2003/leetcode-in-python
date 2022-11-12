# -*- coding: utf-8 -*-
class Solution(object):
    def isMatch(self, s, p):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: previous solution
        Perf: Runtime: 52 ms, faster than 71.65% / Memory Usage: 7 MB, less than 96.37%
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 1. if s[i] == p[j] or p[j] == '.': DP[i][j] == DP[i-1][j-1]
        # 2. if p[j] == '*':
        #       DP[i][j] = DP[i][j-2] ||
        #                   DP[i-1][j] if s[i] == p[j-1] or p[j-1] == '.'
        # 3. false
        m = len(s)+1
        n = len(p)+1
        DP = [[False for _ in range(n)] for _ in range(m)]
        DP[0][0] = True
        for i in range(1,m):
            DP[i][0] = False
        for j in range(1, n):
            if p[j-1] == '*':
                DP[0][j] = DP[0][j-2]
        for i in range(1, m):
            for j in range(1, n):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] == '*':
                    if DP[i][j-2]:
                        DP[i][j] = True
                    elif s[i-1] == p[j-2] or p[j-2] == '.':
                        DP[i][j] = DP[i-1][j]
                    else:
                        DP[i][j] = False
                else:
                    DP[i][j] = False
        return DP[-1][-1]