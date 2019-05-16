# -*- coding: utf-8 -*-
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        DP = [[float('inf') for _ in range(2)] for _ in range(len(A))]
        # DP[i][0] --> no swap
        # DP[i][1] --> swap

        DP[0][0], DP[0][1] = 0, 1
        for i in range(1, len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                DP[i][0] = DP[i-1][0] # no swap
                DP[i][1] = DP[i-1][1] + 1 # since A[i] > A[i-1] and B[i] > B[i-1], if swap i which means i-1 also need swap
            if A[i] > B[i-1] and B[i] > A[i-1]:
                DP[i][0] = min(DP[i][0], DP[i-1][1])
                DP[i][1] = min(DP[i][1], DP[i-1][0]+1)
        return min(DP[-1][0], DP[-1][1])


A = [1,3,5,4]
B = [1,2,3,7]

print Solution().minSwap(A, B)