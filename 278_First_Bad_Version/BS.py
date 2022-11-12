# -*- coding: utf-8 -*-
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(log(n))
        Inspired By: MySELF!!
        :type n: int
        :rtype: int
        """
        def find(l, r):
            if l == r:
                return l
            mid = (l+r)/2
            if isBadVersion(mid):
                return find(l, mid)
            else:
                return find(mid+1, r)
        l = 0
        r = n
        return find(l, r)
