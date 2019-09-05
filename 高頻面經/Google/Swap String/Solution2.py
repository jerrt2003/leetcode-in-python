# -*- coding: utf-8 -*-
class Solution(object):
    def checkSwapOnce(self, s1, s2):
        diff_idx = []
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_idx.append(i)
        if len(diff_idx) != 2:
            return False
        id1, id2 = diff_idx
        s1 = list(s1)
        s1[id1],s1[id2] = s1[id2],s1[id1]
        return s1 == list(s2)

#s1 = 'converse'
#s2 = 'consreve'
s1 = 'abc'
s2 = 'acb'
assert Solution().checkSwapOnce(s1, s2) == True