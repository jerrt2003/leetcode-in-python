# -*- coding: utf-8 -*-
class Solution(object):
    def isPerfectSquare(self, num):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        TP:
        - m = (l+r)/2
        - if m*m > num --> square root must smaller than m and vice versa
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1: return True
        l, r = 0, num
        while l <= r:
            m = (l+r)/2
            if m*m == num:
                return True
            elif m*m > num:
                r = m
            else:
                l = m+1
        return False


num = 9
print Solution().isPerfectSquare(num)