# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, A, B):
        mA,nA,nB = len(A),len(A[0]),len(B[0])
        res = [[0]*len(B[0]) for _ in xrange(mA)]
        for i in xrange(mA):
            for j in xrange(nA):
                if A[i][j]:
                    for k in xrange(nB):
                        res[i][k] += A[i][j]*B[j][k]
        return res