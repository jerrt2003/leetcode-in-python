# -*- coding: utf-8 -*-
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        Solution: 2-D DP Solution
        Time Complexity:
        Space Complexity:
        Inspired By: https://www.youtube.com/watch?v=ih2OZ9-M3OM
                     https://leetcode.com/problems/interleaving-string/solution/
        Algorithm:
            if S3[i+j] == S1[i]: #我等於最後一個字母
                T[i][j] = T[i-1[j] #則只要我前面(i-1)的字串也是interleaving則我也是interleaving
            if S3[i+j] == S2[j]:
                T[i][j] = T[i][j-1]
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 + len_s2 != len(s3): return False
        DP = [[False for _ in range(len_s2+1)] for _ in range(len_s1+1)]
        for i in range(len_s1+1):
            for j in range(len_s2+1):
                l = i + j - 1
                if i == 0 and j == 0:
                    DP[i][j] = True
                elif i == 0:
                    if s3[l] is s2[j-1]:
                        DP[i][j] = DP[i][j-1]
                elif j == 0:
                    if s3[l] is s1[i-1]:
                        DP[i][j] = DP[i-1][j]
                else:
                    if s3[l] is s1[i-1]:
                        DP[i][j] = DP[i-1][j] or DP[i][j]
                    if s3[l] is s2[j-1]:
                        DP[i][j] = DP[i][j-1] or DP[i][j]
        return DP[-1][-1]

#s1 = "aabcc"
#s2 = "dbbca"
#s3 = "aadbbcbcac"

s1 = "ab"
s2 = "bc"
s3 = "babc"

sol = Solution()
print sol.isInterleave(s1,s2,s3)

