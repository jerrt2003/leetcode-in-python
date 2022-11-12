# -*- coding: utf-8 -*-
class Solution(object):
    def findLongestChain(self, input, wordDict):
        self.wordDict = set(wordDict)
        self.longestMap = dict()
        self.res = -float('inf')
        m = len(input)
        for i in range(m):
            new_word = input[0:i]+input[i+1:m]
            if new_word in self.wordDict:
                self.res = max(self.res, self._findLongest(new_word))

    def _findLongest(self, input):
        if input is None:
            return 0
        if input in self.longestMap:
            return self.longestMap[input]
        m = len(input)
        for i in range(m):
            new_word = input[0:i] + input[i+1:m]
            if new_word in self.wordDict:
                self.longestMap[input] = 1 + self._findLongest(new_word)
        return self.longestMap[input]


