# -*- coding: utf-8 -*-
import sys
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        left = 1
        right = sys.maxint
        while True:
            mid = (left+right)/2
            if mid*mid > x:
                right = mid-1
            else:
                if (mid+1)*(mid+1) > x:
                    return mid
                left = mid+1

x = 0
print Solution().mySqrt(x)