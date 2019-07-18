# -*- coding: utf-8 -*-
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        i, j = 0, len(A)-1
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                res.insert(0, A[i]*A[i])
                i += 1
            else:
                res.insert(0, A[j]*A[j])
                j -= 1
        return res