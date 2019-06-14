# -*- coding: utf-8 -*-
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        Sol: BS
        Time: O(log(n))
        Space: O(1)
        Perf: Runtime: 20 ms, faster than 64.35% / Memory Usage: 11.8 MB, less than 36.19%
        :type n: int
        :rtype: int
        """
        l, r  = 1, n+1
        while l < r:
            mid = (l+r-1)/2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid+1
        return n if l == n+1 else l