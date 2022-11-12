# -*- coding: utf-8 -*-
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        l, r = 0, n
        while l < r:
            m = (l + r) / 2
            res += m
            l = m + 1
        return res

