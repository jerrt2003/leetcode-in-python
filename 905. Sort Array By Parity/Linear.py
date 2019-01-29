# -*- coding: utf-8 -*-
class Solution(object):
    def sortArrayByParity(self, A):
        """
        Solution: Linear
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!! (88ms, beat 91.73%)
        TP:
        - to record the last odd index and replace it with the next even number
        :type A: List[int]
        :rtype: List[int]
        """
        last_odd = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[last_odd], A[i] = A[i], A[last_odd]
                last_odd += 1
        return A
