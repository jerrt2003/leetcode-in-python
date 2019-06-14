# -*- coding: utf-8 -*-
class Solution(object):
    def newSort(self, wordList, alienWord):
        order = dict()
        for i, v in enumerate(alienWord, 0):
            order[v] = i
        return sorted(wordList, key=lambda word: [order[char] for char in word])

assert Solution().newSort(["aa","ab","bc","bce"], ['b','c', 'a','e']) == ["bc","bce","ab","aa"]