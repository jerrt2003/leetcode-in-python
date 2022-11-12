# -*- coding: utf-8 -*-
class Solution(object):
    def findLength(self, A, B):
        """
        Solution: DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: https://leetcode.com/problems/maximum-length-of-repeated-subarray/solution/ (approach 3)
        TP:
        - Instead of counting max_common_len from beginning, we can do it backwards
        - DP[i][j] represent max_common_len for A[i:] and B[j:]
        - If A[i] == B[j], then:
            - DP[i][j] = DP[i+1][j+1] + 1 (since DP[i+1][j+1] stands for common length as well)
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        MAX_COMM = 0
        DP = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        for i in range(len(B)-1, -1, -1):
            for j in range(len(A)-1, -1, -1):
                if B[i] == A[j]:
                    DP[i][j] = DP[i+1][j+1] + 1
                    MAX_COMM = max(MAX_COMM, DP[i][j])
        return MAX_COMM

#A= [1,2,3,2,1]
#B= [3,2,1,4,7]
A = [1]
B = [2]

print Solution().findLength(A, B)