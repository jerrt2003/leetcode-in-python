# -*- coding: utf-8 -*-
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

import random
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            guess = random.choice(wordlist)
            n = master.guess(guess)
            nextWordList = []
            for word in wordlist:
                k = 0
                for i, j in zip(guess, word):
                    if i == j:
                        k += 1
                if k == n:
                    nextWordList.append(word)
            wordlist = nextWordList