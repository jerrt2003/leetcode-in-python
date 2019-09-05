# -*- coding: utf-8 -*-
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        Perf: Runtime: 12 ms, faster than 97.45% / Memory Usage: 12 MB, less than 23.53%
        T: O(n)
        S: O(n)
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenS = len(s)
        lenT = len(t)
        if lenS > lenT:
            return self.isOneEditDistance(t, s)

        if lenT - lenS > 1:
            return False

        for i in range(lenS):
            if s[i] != t[i]:
                if lenS == lenT:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]

        return lenS + 1 == lenT