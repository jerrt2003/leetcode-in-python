# -*- coding: utf-8 -*-
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps = {}
        for _s, _t in zip(s, t):
            if maps.setdefault(_s, _t) != _t:
                return False
        return len(set(maps.values())) == len(maps.values())
