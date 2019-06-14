# -*- coding: utf-8 -*-
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        Solution: using sort
        Perf: Runtime: 24 ms, faster than 70.63% / Memory Usage: 11.7 MB, less than 63.57%
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderMaps = dict()
        for k, v in enumerate(order, 0):
            orderMaps[v] = k
        return words == sorted(words, key=lambda word: [orderMaps[c] for c in word])

