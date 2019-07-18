# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(t)
        bkt = collections.defaultdict(int)
        p1, p2, minDist, res, formed = 0, 0, float('inf'), '', 0
        while p2 < len(s):
            if s[p2] in counter:
                bkt[s[p2]] += 1
                if bkt[s[p2]] == counter[s[p2]]:
                    formed += 1
            while formed == len(counter):
                if p2 - p1 + 1 < minDist:
                    res = s[p1:p2 + 1]
                    minDist = p2 - p1 + 1
                if s[p1] in counter:
                    bkt[s[p1]] -= 1
                    if bkt[s[p1]] < counter[s[p1]]:
                        formed -= 1
                p1 += 1
            p2 += 1
        return res


assert Solution().minWindow("ADOBECODEBANC","CODEB") == "DOBEC"