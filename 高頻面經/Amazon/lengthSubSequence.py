# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def findLen(self, inputList):
        res = []
        start = hash2.defaultdict(int)
        end = hash2.defaultdict(int)
        k = []
        m = len(inputList)
        for i in range(m):
            if inputList[i] not in start.keys():
                start[inputList[i]] = i
                k.append(inputList[i])
            end[inputList[i]] = i



print Solution().findLen(['a','b','c','a'])
