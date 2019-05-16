# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        window = dict()
        while r < len(s):
            while len(window) > 3:
                window[s[l]].pop(0)
                if not window[s[l]]:
                    del window[s[l]]
                l += 1
            if s[r] in t:
                window[s[r]].append(r)
            r += 1
