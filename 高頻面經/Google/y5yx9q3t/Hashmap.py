# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def findExclusive(self, A, B):
        counterA = collections.Counter(A)
        counterB = collections.Counter(B)
        resA = []
        for k, v in counterA.iteritems():
            if k in counterB:
                rep = max(0, v - counterB[k])
                resA += [k for _ in range(rep)]
            else:
                resA += [k for _ in range(v)]
        resB = []
        for k, v in counterB.iteritems():
            if k in counterA:
                rep = max(0, v - counterA[k])
                resB += [k for _ in range(rep)]
            else:
                resB += [k for _ in range(v)]
        return resA, resB

assert Solution().findExclusive([1,2,2,2,3,4],[2,5])
