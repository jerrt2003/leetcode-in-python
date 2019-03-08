# -*- coding: utf-8 -*-
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m1 = len(s1)
        m2 = len(s2)
        m3 = len(s3)
        if m1 + m2 != m3: return False
        DP = [[False for _ in range(m2 + 1)] for _ in range(m1 + 1)]
        for i in range(m1 + 1):
            for j in range(m2 + 1):
                k = i + j - 1
                if i == 0 and j == 0:
                    DP[i][j] = True
                elif i == 0:
                    if s2[j - 1] == s3[k]:
                        DP[0][j] = DP[0][j - 1]
                elif j == 0:
                    if s1[i - 1] == s3[k]:
                        DP[i][0] = DP[i - 1][0]
                else:
                    if s1[i - 1] == s3[k]:
                        DP[i][j] = DP[i - 1][j] or DP[i][j] # ***
                    if s2[j - 1] == s3[k]:
                        DP[i][j] = DP[i][j - 1] or DP[i][j] # !! need to add 'or DP[i][j]' to preserve previous *** result
        return DP[-1][-1]

s1 = "aabc"
s2 = "abad"
s3 = "aabadabc"

print Solution().isInterleave(s1, s2, s3)