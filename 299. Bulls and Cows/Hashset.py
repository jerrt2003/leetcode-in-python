# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s_set = collections.Counter(secret)
        g_set = collections.Counter(guess)
        available = {}
        for char in g_set:
            available[char] = min(s_set[char], g_set[char])
        check = zip(secret, guess)
        res = {}





secret = "1122"
guess = "1222"

print Solution().getHint(secret,guess)