# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, A, B):
        """
        T: O(m*n + n*p + (m*n)*(n*p))
        S: O(m*n + n*p)
        Perf: Runtime: 40 ms, faster than 88.90% / Memory Usage: 12.1 MB, less than 16.67%
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        out = [[0] * len(B[0]) for _ in range(len(A))]

        def findNonZero(m):
            res = []
            for i in range(len(m)):
                for j in range(len(m[0])):
                    if m[i][j]:
                        res.append([i, j])
            return res

        nonZeroA = findNonZero(A)
        nonZeroB = findNonZero(B)

        for elemB in nonZeroB:
            rowB = elemB[0]
            for elemA in nonZeroA:
                colA = elemA[1]
                if rowB == colA:
                    out[elemA[0]][elemB[1]] += A[elemA[0]][elemA[1]] * B[elemB[0]][elemB[1]]

        return out

