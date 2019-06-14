# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        require = collections.Counter(t)
        pt1, pt2 = 0,