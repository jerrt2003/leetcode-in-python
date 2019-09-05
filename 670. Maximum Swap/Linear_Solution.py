# -*- coding: utf-8 -*-
class Solution(object):
    def maximumSwap(self, num):
        """
        Sol: O(n) Solution
        Perf: Runtime: 20 ms, faster than 40.34% / Memory Usage: 11.8 MB, less than 60.00%
        T: O(n)
        S: O(n)
        Key: map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
        :type num: int
        :rtype: int
        """
        A = map(int, str(num)) # only string can be iterable
        lastIdx = {x:i for i, x in enumerate(A)} # find the occurrence of lastIdx of each 'digit'
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if lastIdx.get(d, None) > i:
                    A[i], A[lastIdx[d]] = A[lastIdx[d]], A[i]
                    return int(''.join(map(str, A)))
        return num