# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def findLen(self, inputList):
        res = []
        start = collections.defaultdict(int)
        end = collections.defaultdict(int)
        k = []
        m = len(inputList)
        for i in range(m):
            if inputList[i] not in start.keys():
                start[inputList[i]] = i
                k.append(inputList[i])
            end[inputList[i]] = i



print Solution().findLen(['a','b','c','a'])
