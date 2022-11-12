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

import collections
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
            countCheck = collections.defaultdict(list)
            for w1 in wordlist:
                k = 0
                for w2 in wordlist:
                    count = self.match(w1, w2)
                    if count == 0:
                        k += 1
                countCheck[k].append(w1)
            wordlist = countCheck[min(countCheck.keys())]
            guess = random.choice(wordlist)
            n = master.guess(guess)
            nextWordList = []
            for word in wordlist:
                k = 0
                for w1, w2 in zip(guess, wordlist):
                    if w1 == w2:
                        k += 1
                if k == n:
                    nextWordList.append(word)
            wordlist = nextWordList




    def match(self, word1, word2):
        count = 0
        for w1, w2 in zip(word1, word2):
            if w1 == w2:
                count += 1
        return count