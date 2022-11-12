# -*- coding: utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
        """
        Solution: Fast Pow
        Time Complexity: O(log(n))
        Space Complexity: O(log(n))
        Inspired By: https://leetcode.com/problems/powx-n/solution/
        :type x: float
        :type n: int
        :rtype: float
        """
        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n/2)
            if n % 2 == 0:
                return half*half
            else:
                return half*half*x

        if n < 0:
            x = 1/x
            n = -n
        return fastPow(x, n)


x= 2.00000
n = -2

print Solution().myPow(x, n)