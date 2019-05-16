# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        DP = [[None for _ in range(m)] for _ in range(m)]

        def DFS(i, j):
            if DP[i][j]: return DP[i][j]
            if i == j:
                DP[i][j] = True
            elif j-i+1 == 2:
                if s[i] == s[j]:
                    DP[i][j] = True
                else:
                    DP[i][j] = False
            else:
                if DFS(i+1, j-1) and s[i] == s[j]:
                    DP[i][j] = True
                else:
                    DP[i][j] = False
            return DP[i][j]

        max_len = -float('inf')
        res = None
        for i in range(m):
            for j in range(i, m):
                if DFS(i, j):
                    curr_len = j-i+1
                    if curr_len > max_len:
                        max_len = curr_len
                        res = s[i:j+1]

        return res





s = 'cb'
print Solution().longestPalindrome(s)