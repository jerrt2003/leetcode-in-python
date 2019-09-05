# -*- coding: utf-8 -*-
class Solution(object):
    def isMonotonic(self, A):
        """
        Perf: Runtime: 464 ms, faster than 33.91% / Memory Usage: 17.1 MB, less than 36.36%
        T: O(n)
        S: O(1)
        :type A: List[int]
        :rtype: bool
        """
        incr = decr = True
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                decr = False
            if A[i] < A[i + 1]:
                incr = False

        return incr or decr
