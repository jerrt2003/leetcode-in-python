# -*- coding: utf-8 -*-
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # DP[i][j] := max score at i with K partition
        m = len(A)
        DP = [[0 for _ in range(K+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,K+1):
                for pos in range(i):
                    DP[i][j] = max(DP[i][j], DP[pos][j-1] + float(sum(A[pos:i]))/len(A[pos:i]))
        return DP[-1][-1]


#A = [9,1,2,3,9]
#K = 3

A = [1,2,3,4,5,6,7]
K = 4

print Solution().largestSumOfAverages(A, K)