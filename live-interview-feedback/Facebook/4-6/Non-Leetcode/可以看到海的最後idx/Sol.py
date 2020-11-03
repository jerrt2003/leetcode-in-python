# -*- coding: utf-8 -*-
class Solution(object):
    def findLastIdx(self, data):
        height = -float('inf')
        res = len(data)-1
        for h, idx in data[::-1]:
            if h > height:
                height = h
                res = idx
        return res