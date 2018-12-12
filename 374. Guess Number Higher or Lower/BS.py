# -*- coding: utf-8 -*-
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    pass

class Solution(object):
    def guessNumber(self, n):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(log(n))
        Inspired By: MySELF!!
        :type n: int
        :rtype: int
        """
        def getAns(l, r):
            m = (l+r)/2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                return getAns(l, m-1)
            else:
                return getAns(m+1, r)

        return getAns(1, n)
